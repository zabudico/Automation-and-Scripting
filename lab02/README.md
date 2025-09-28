# Взаимодействие с Web API с помощью скрипта Python

## 📋 Описание проекта
Данный проект представляет собой Python скрипт для получения курсов валют через Web API. 
Скрипт взаимодействует с локальным API сервисом, получает данные о курсах валют на указанные даты и сохраняет их в формате JSON.

## 🎯 Цель задания
Научиться взаимодействовать с веб-API с помощью скрипта Python.

## 📁 Структура проекта

```
lab02/
├── currency_exchange_rate.py    # Основной скрипт
├── test_multiple_dates.py       # Скрипт для тестирования
├── README.md                    # Документация
├── error.log                    # Лог ошибок
└── data/                        # Директория с данными
    ├── EUR_RON_2025-05-31.json
    ├── EUR_RON_2025-07-15.json
    ├── EUR_USD_2025-02-20.json
    ├── EUR_USD_2025-03-15.json
    ├── MDL_EUR_2025-02-28.json
    └── MDL_USD_2025-09-08.json
    ├ ...
    └── USD_MDL_2025-05-01.json
```

## 🎯 Выполнение задания

### ✅ Подготовка
- Скачан и распакован проект `lab02prep.zip`.
- Запущен API сервис с использованием Docker, следуя инструкциям в  README.md файле.
- Сервис доступен по адресу `http://localhost:8080`.

### ✅ Создание структуры
- Создана ветка `lab02` в проекте автоматизации.
- Создана директория `lab02`.
- Создан файл `currency_exchange_rate.py`.

### ✅ Функциональность скрипта

#### Получение курса валют через командную строку
Скрипт принимает три обязательных параметра:
- Исходная валюта
- Целевая валюта
- Дата в формате ГГГГ-ММ-ДД

```bash
python currency_exchange_rate.py USD EUR 2025-01-01
```

<img width="1773" height="583" alt="image" src="https://github.com/user-attachments/assets/88b619a2-1b1c-4921-90a8-53888d349771" />


#### Сохранение данных в JSON формате
- Данные сохраняются в папку `data/`
- Автоматическое создание директории при необходимости
- Формат имен файлов: `{валюта1}_{валюта2}_{дата}.json`
- Пример: data/USD_EUR_2025-01-01.json

#### Обработка ошибок
- Вывод понятных сообщений в консоль
- Логирование ошибок в файл `error.log`
- Обработка различных типов ошибок:
  - Сетевые ошибки (недоступность API)
  - Неверные параметры (неподдерживаемые валюты)
  - Неверные даты (вне диапазона)
  - Ошибки API

### ✅ Тестирование
Протестировано с 6 датами в диапазоне 2025-01-01 - 2025-09-15 с равными интервалами:

| № | Дата | Валютная пара | Интервал |
|---|------|---------------|----------|
| 1 | 2025-01-01 | USD → EUR | Базовая дата |
| 2 | 2025-02-20 | EUR → USD | 50 дней |
| 3 | 2025-04-11 | USD → MDL | 51 день |
| 4 | 2025-05-31 | EUR → RON | 50 дней |
| 5 | 2025-07-20 | USD → EUR | 50 дней |
| 6 | 2025-09-08 | MDL → USD | 50 дней |

### ✅ Документация
Создан файл `readme.md` с описанием:
- Установка зависимостей (`pip install requests`)
- Примеры запуска скрипта
- Описание структуры и основных функций

## 🔧 Техническая реализация

### Основные функции скрипта

```python
def get_exchange_rate(from_currency, to_currency, date)
    # Получение данных от API

def validate_date(date_string)
    # Валидация даты и диапазона

def validate_currencies(from_currency, to_currency)
    # Проверка поддерживаемых валют

def save_to_file(data, from_currency, to_currency, date)
    # Сохранение в JSON файл

def setup_logging()
    # Настройка логирования ошибок
```

### Пример использования
```bash
python currency_exchange_rate.py USD EUR 2025-01-01
```

**Вывод:**
```
=== Currency Exchange Rate Script ===
Parameters: USD -> EUR on 2025-01-01
Requesting rate: USD -> EUR for 2025-01-01

=== Exchange Rate ===
From: USD
To: EUR
Date: 2025-01-01
Rate: 1.0449967801462194
[SUCCESS] Data saved to: data/USD_EUR_2025-01-01.json

[SUCCESS] Operation completed successfully!
```

<img width="1773" height="583" alt="image" src="https://github.com/user-attachments/assets/3dfebb9c-704a-48a8-a26f-bd4400ff505e" />


## 📊 Результаты тестирования API

### Проверка через curl:
```bash
# Список валют
curl "http://localhost:8080/?currencies" -X POST -d "key=myapi123"
# Ответ: {"error":"","data":["MDL","USD","EUR","RON","RUS","UAH"]}

<img width="1788" height="168" alt="image" src="https://github.com/user-attachments/assets/e7760afd-0f33-4f0e-931e-d6ceb510378d" />


# Курс обмена
curl "http://localhost:8080/?from=USD&to=EUR&date=2025-01-01" -X POST -d "key=myapi123"
# Ответ: {"error":"","data":{"from":"USD","to":"EUR","rate":1.0449967801462194,"date":"2025-01-01"}}
```

<img width="1779" height="173" alt="image" src="https://github.com/user-attachments/assets/38ae2da3-143d-4633-8a27-3443193a34a7" />


### Обработка ошибок:
```bash
# Неверный API ключ
curl "http://localhost:8080/?currencies" -X POST -d "key=wrongkey"
# Ответ: {"error":"Invalid API key","data":[]}

<img width="1783" height="173" alt="image" src="https://github.com/user-attachments/assets/35ace343-c7db-4213-b697-3806dc550940" />


# Неверная валюта
curl "http://localhost:8080/?from=XXX&to=YYY&date=2025-01-01" -X POST -d "key=myapi123"
# Ответ: {"error":"The currency XXX is unknown","data":[]}
```

<img width="1778" height="169" alt="image" src="https://github.com/user-attachments/assets/0be9d601-fabe-4b53-9919-9b97e576c088" />


## 🚀 Запуск проекта

### Требования
- Python 3.6+
- Установленная библиотека requests
- Запущенный Docker контейнер с API

### Установка
```bash
pip install requests
```

### Запуск API
```bash
cd IW02-Creating_a_Python_Script_to_Interact_with_an_API\lab02prep
cp sample.env .env
docker-compose up -d
```

`cd IW02-Creating_a_Python_Script_to_Interact_with_an_API\lab02prep` - переход в папку с сервисом.

`cp sample.env .env` - создается рабочий файл настроек из шаблона, чтобы Docker знал, какой API-ключ использовать.Нужно не забыть указать свой ключ.

`docker compose up -d` — поднимает все сервисы из файла docker-compose.yaml и запустить их в фоне. 

## 📈 Статус выполнения

- ✅ Все требования задания выполнены
- ✅ Скрипт протестирован с различными параметрами
- ✅ Реализована обработка ошибок
- ✅ Создана документация
- ✅ Код загружен в GitHub репозиторий

## 🎯 Итог

Задание успешно выполнено. Создан рабочий Python скрипт для взаимодействия с Web API, который:
- Получает курсы валют через параметры командной строки
- Сохраняет данные в JSON файлы
- Обрабатывает ошибки и логирует их
- Протестирован с различными параметрами
- Полностью соответствует требованиям задания

**Проект готов к сдаче.** ✅

