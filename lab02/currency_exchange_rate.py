#!/usr/bin/env python3
"""
Currency Exchange Rate Script
Gets exchange rates from local API and saves to JSON files
"""

import requests
import json
import sys
import argparse
from datetime import datetime, timedelta
import os
import logging

# Configuration
BASE_URL = "http://localhost:8080"
API_KEY = "myapi123"

def setup_logging():
    """Setup error logging"""
    logging.basicConfig(
        filename='error.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def create_data_directory():
    """Create data directory if it doesn't exist"""
    if not os.path.exists('data'):
        os.makedirs('data')

def validate_date(date_string):
    """Validate date format and range"""
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        
        # Check date range
        start_date = datetime(2025, 1, 1)
        end_date = datetime(2025, 9, 15)
        
        if not (start_date <= date_obj <= end_date):
            raise ValueError(f"Date must be between 2025-01-01 and 2025-09-15")
            
        return date_string
    except ValueError as e:
        raise ValueError(f"Invalid date: {date_string}. Use YYYY-MM-DD format. {e}")

def get_available_currencies():
    """Get list of available currencies from API"""
    try:
        response = requests.post(
            f"{BASE_URL}/?currencies",
            data={"key": API_KEY},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        if data.get('error'):
            raise Exception(f"API Error: {data['error']}")
            
        return data['data']
    except Exception as e:
        print(f"Warning: Could not fetch available currencies: {e}")
        return ['USD', 'EUR', 'MDL', 'RON', 'RUS', 'UAH']  # Fallback

def validate_currencies(from_currency, to_currency):
    """Validate currency codes"""
    available_currencies = get_available_currencies()
    
    if from_currency not in available_currencies:
        raise ValueError(f"Invalid source currency: {from_currency}. Available: {available_currencies}")
    
    if to_currency not in available_currencies:
        raise ValueError(f"Invalid target currency: {to_currency}. Available: {available_currencies}")

def get_exchange_rate(from_currency, to_currency, date):
    """Get exchange rate from API"""
    try:
        print(f"Requesting rate: {from_currency} -> {to_currency} for {date}")
        
        response = requests.post(
            f"{BASE_URL}/?from={from_currency}&to={to_currency}&date={date}",
            data={"key": API_KEY},
            timeout=10
        )
        
        response.raise_for_status()
        data = response.json()
        
        if data.get('error'):
            error_msg = f"API Error: {data['error']}"
            logging.error(error_msg)
            raise Exception(error_msg)
            
        return data
        
    except requests.exceptions.ConnectionError:
        error_msg = "Cannot connect to API. Make sure Docker container is running on localhost:8080"
        logging.error(error_msg)
        raise Exception(error_msg)
    except requests.exceptions.Timeout:
        error_msg = "API request timed out"
        logging.error(error_msg)
        raise Exception(error_msg)
    except Exception as e:
        error_msg = f"Request failed: {e}"
        logging.error(error_msg)
        raise Exception(error_msg)

def save_to_file(data, from_currency, to_currency, date):
    """Save data to JSON file"""
    filename = f"data/{from_currency}_{to_currency}_{date}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[SUCCESS] Data saved to: {filename}")
        return filename
    except IOError as e:
        error_msg = f"Error saving file: {e}"
        logging.error(error_msg)
        raise Exception(error_msg)

def main():
    """Main function"""
    print("=== Currency Exchange Rate Script ===")
    
    parser = argparse.ArgumentParser(
        description='Get currency exchange rates for specified date (2025-01-01 to 2025-09-15)',
        epilog='Example: python currency_exchange_rate.py USD EUR 2025-01-01'
    )
    
    parser.add_argument(
        'from_currency',
        type=str.upper,
        help='Source currency code (USD, EUR, MDL, RON, RUS, UAH)'
    )
    
    parser.add_argument(
        'to_currency', 
        type=str.upper,
        help='Target currency code (USD, EUR, MDL, RON, RUS, UAH)'
    )
    
    parser.add_argument(
        'date',
        type=validate_date,
        help='Date in YYYY-MM-DD format (between 2025-01-01 and 2025-09-15)'
    )
    
    try:
        args = parser.parse_args()
        
        # Validate currencies
        validate_currencies(args.from_currency, args.to_currency)
        
        print(f"Parameters: {args.from_currency} -> {args.to_currency} on {args.date}")
        
        # Setup
        setup_logging()
        create_data_directory()
        
        # Get exchange rate
        exchange_data = get_exchange_rate(args.from_currency, args.to_currency, args.date)
        
        # Display results
        if 'data' in exchange_data:
            rate_data = exchange_data['data']
            print(f"\n=== Exchange Rate ===")
            print(f"From: {args.from_currency}")
            print(f"To: {args.to_currency}")
            print(f"Date: {rate_data.get('date', 'N/A')}")
            print(f"Rate: {rate_data.get('rate', 'N/A')}")
        
        # Save to file
        filename = save_to_file(exchange_data, args.from_currency, args.to_currency, args.date)
        
        print(f"\n[SUCCESS] Operation completed successfully!")
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()