# IW02: Creating a Python Script to Interact with an API

Взаимодействие с Web API с помощью скрипта Python

## Выполнил

- Zabudico Alexandr I-2302
- Дата выполнения: 28.09.2025


## 📋 Описание проекта
Данный проект представляет собой Python скрипт для получения курсов валют через Web API. 
Скрипт взаимодействует с локальным API сервисом, получает данные о курсах валют на указанные даты и сохраняет их в формате JSON.

## 🎯 Цель задания
Научиться взаимодействовать с веб-API с помощью скрипта Python.

## Задача
В  `automation` проекте создайте ветку с именем  `lab02`. Создайте каталог с именем  `lab02`. Внутри него создайте файл с именем  `currency_exchange_rate.py`.

Напишите скрипт на Python ( `currency_exchange_rate.py`), который будет взаимодействовать с API сервиса. Скрипт должен выполнять следующие функции:

1. Получите обменный курс одной валюты по отношению к другой на указанную дату. Валюты и дата должны быть переданы как параметры командной строки.
2. Сохраните полученные данные в файл в формате JSON. Имя файла должно включать валюты и дату запроса. Сохраните файл в  data каталоге, который необходимо создать в корне проекта, если он ещё не существует.
3. Обрабатывайте ошибки, возникающие при запросах к API (например, недопустимые параметры). Выводите понятные сообщения об ошибках в консоль и сохраняйте их в файл журнала  error.log в корне проекта.

Протестируйте скрипт, запустив его с разными параметрами. Период данных: с  2025-01-01 по  2025-09-15.

Запустите скрипт для дат в выбранном вами диапазоне (не менее 5 дат с равными интервалами).

Создайте файл  readme.md и опишите:
- Как установить необходимые зависимости для запуска скрипта;
- Как запустить скрипт с примерами команд;
- Как структурирован скрипт (основные функции и логика).

## Подготовка
Скачайте проект, прикреплённый к этому заданию, и распакуйте его в удобное место. Запустите сервис, следуя инструкциям в  README.md файле.

## 📁 Структура проекта

```
lab02/
├── currency_exchange_rate.py    # Основной скрипт
├── test_multiple_dates.py       # Скрипт для тестирования
├── README.md                    # Документация
├── error.log                    # Лог ошибок
├── sample.env                   # Образец настройки переменной окружения
└── data/                        # Директория с данными
    ├── EUR_RON_2025-05-31.json
    ├── EUR_RON_2025-07-15.json
    ├── EUR_USD_2025-02-20.json
    ├── EUR_USD_2025-03-15.json
    ├── MDL_EUR_2025-02-28.json
    └── MDL_USD_2025-09-08.json
    ├   ...
    └── USD_MDL_2025-05-01.json
```

## 🎯 Выполнение задания

### ✅ Подготовка
- Скачан и распакован проект `lab02prep.zip`.
- Запущен API сервис с использованием Docker, следуя инструкциям: 
- Сервис доступен по адресу `http://localhost:8080`.

  <img width="548" height="153" alt="image" src="https://github.com/user-attachments/assets/4b9da6d7-95dd-4539-b62b-f0c19d1315c4" />


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


```bash
# 1. Неверная валюта (должна записаться в error.log)
python currency_exchange_rate.py XXX USD 2025-01-01

# 2. Неверная дата (должна записаться в error.log)  
python currency_exchange_rate.py USD EUR 2024-12-31

# 3. Неверный формат даты (должна записаться в error.log)
python currency_exchange_rate.py USD EUR 2025/01/01

# 4. Одинаковые валюты (должна записаться в error.log)
python currency_exchange_rate.py USD USD 2025-01-01

# 5. Успешный запрос
python currency_exchange_rate.py USD EUR 2025-01-01
```

<img width="1405" height="224" alt="image" src="https://github.com/user-attachments/assets/7e633884-1391-460c-9994-37b57ea530cf" />


```bash

C:\Users\User\Desktop\Automation-and-Scripting\lab02>python currency_exchange_rate.py XXX USD 2025-01-01
=== Currency Exchange Rate Script ===
Parameters: XXX -> USD on 2025-01-01
Supported currencies: MDL, USD, EUR, RON, RUS, UAH

2025-09-28 21:28:50,578 - ERROR - Invalid source currency: XXX. Available: ['MDL', 'USD', 'EUR', 'RON', 'RUS', 'UAH']
[ERROR] Invalid source currency: XXX. Available: ['MDL', 'USD', 'EUR', 'RON', 'RUS', 'UAH']

C:\Users\User\Desktop\Automation-and-Scripting\lab02>python currency_exchange_rate.py USD EUR 2024-12-31
=== Currency Exchange Rate Script ===
Parameters: USD -> EUR on 2024-12-31
Supported currencies: MDL, USD, EUR, RON, RUS, UAH

2025-09-28 21:28:54,782 - ERROR - Date 2024-12-31 is out of range. Must be between 2025-01-01 and 2025-09-15
[ERROR] Date 2024-12-31 is out of range. Must be between 2025-01-01 and 2025-09-15

C:\Users\User\Desktop\Automation-and-Scripting\lab02>python currency_exchange_rate.py USD EUR 2025/01/01
=== Currency Exchange Rate Script ===
Parameters: USD -> EUR on 2025/01/01
Supported currencies: MDL, USD, EUR, RON, RUS, UAH

2025-09-28 21:28:57,198 - ERROR - Invalid date format: 2025/01/01. Use YYYY-MM-DD
[ERROR] Invalid date format: 2025/01/01. Use YYYY-MM-DD

C:\Users\User\Desktop\Automation-and-Scripting\lab02>
C:\Users\User\Desktop\Automation-and-Scripting\lab02>python currency_exchange_rate.py USD USD 2025-01-01
=== Currency Exchange Rate Script ===
Parameters: USD -> USD on 2025-01-01
Supported currencies: MDL, USD, EUR, RON, RUS, UAH

2025-09-28 21:29:03,646 - ERROR - Source and target currencies cannot be the same: USD
[ERROR] Source and target currencies cannot be the same: USD

C:\Users\User\Desktop\Automation-and-Scripting\lab02>python currency_exchange_rate.py USD EUR 2025-01-01
=== Currency Exchange Rate Script ===
Parameters: USD -> EUR on 2025-01-01
Supported currencies: MDL, USD, EUR, RON, RUS, UAH

Requesting rate: USD -> EUR for 2025-01-01

=== Exchange Rate ===
From: USD
To: EUR
Date: 2025-01-01
Rate: 1.0449967801462194
[SUCCESS] Data saved to: data\USD_EUR_2025-01-01.json

[SUCCESS] Operation completed successfully!

C:\Users\User\Desktop\Automation-and-Scripting\lab02>

```


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


# 🚀 Запуск проекта

## Предварительные требования

### Системные требования
- **Python 3.6+** - для работы основного скрипта
- **Библиотека requests** - для HTTP-запросов
- **Docker и Docker Compose** - для запуска API сервиса

## 📋 Пошаговая инструкция запуска

### 1. Запуск API сервиса

**Шаг 1: Подготовка окружения**
```bash
# Перейдите в директорию с API сервисом
cd IW02-Creating_a_Python_Script_to_Interact_with_an_API\lab02prep

# Создайте файл настроек из шаблона
cp sample.env .env
```

**Шаг 2: Настройка API ключа**
Откройте файл `.env` в текстовом редакторе и установите ваш API ключ:
```
API_KEY=myapi123
```

**Шаг 3: Запуск сервиса**
```bash
# Запустите Docker контейнеры в фоновом режиме
docker-compose up -d
```

**Шаг 4: Проверка работоспособности**
```bash
# Проверьте, что API отвечает
curl "http://localhost:8080/?currencies" -X POST -d "key=myapi123"
```
Ожидаемый ответ: `{"error":"","data":["MDL","USD","EUR","RON","RUS","UAH"]}`

### 2. Установка зависимостей для Python скрипта

**Шаг 1: Установка библиотеки requests**
```bash
pip install requests
```

**Шаг 2: Проверка установки**
```bash
python -c "import requests; print('Библиотека requests успешно установлена')"
```

### 3. Запуск основного скрипта

**Шаг 1: Перейдите в директорию скрипта**
```bash
cd C:\Users\User\Desktop\Automation-and-Scripting\lab02
```

**Шаг 2: Запуск скрипта**
```bash
# Базовый синтаксис
python currency_exchange_rate.py FROM_CURRENCY TO_CURRENCY DATE

# Примеры использования
python currency_exchange_rate.py USD EUR 2025-01-01
python currency_exchange_rate.py EUR USD 2025-03-15
python currency_exchange_rate.py USD MDL 2025-06-01
```

## 🎯 Быстрый старт

Если вы хотите быстро проверить работоспособность:

```bash
# 1. Установите зависимости
pip install requests

# 2. Запустите API (в отдельном терминале)
cd IW02-Creating_a_Python_Script_to_Interact_with_an_API\lab02prep
cp sample.env .env
# Отредактируйте .env: API_KEY=myapi123
docker-compose up -d

# 3. Запустите тестовый запрос (в основном терминале)
cd C:\Users\User\Desktop\Automation-and-Scripting\lab02
python currency_exchange_rate.py USD EUR 2025-01-01
```

## 🔧 Проверка работоспособности

После выполнения всех шагов вы должны увидеть:

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

## 📝 Примечания

- **API сервис** должен быть запущен перед использованием скрипта
- **API ключ** в файле `.env` должен совпадать с ключом, используемым в скрипте (`myapi123`)
- **Диапазон дат** поддерживается с 2025-01-01 по 2025-09-15
- **Поддерживаемые валюты**: MDL, USD, EUR, RON, RUS, UAH

## 🆘 Устранение неполадок

Если возникли проблемы:

1. **Проверьте, запущен ли Docker**
2. **Убедитесь, что API доступен**: `curl "http://localhost:8080/?currencies" -X POST -d "key=myapi123"`
3. **Проверьте установку Python библиотек**: `python -c "import requests"`
4. **Убедитесь в правильности API ключа** в файле `.env`

Проект готов к использованию! 🎉


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

## Вывод 

В ходе выполения работы, я ознакомился с тем, как взаимодействовать с Web API с помощью скрипта Python, освежил в памяти, как поднимать контейнеры, работать с API, писать код для этих задач. Считаю данную лабораторную работу полезной для собственного развития, как разработчика.:)












