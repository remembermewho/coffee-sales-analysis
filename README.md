# ☕ Coffee Sales Analysis

Проект для анализа продаж в кофейне Кейптауна (март 2024 – март 2025), построенный на Python.  
С помощью Pandas, Seaborn и Matplotlib визуализируются ключевые показатели:  
продажи по времени суток, дням недели, типу кофе и способу оплаты.

---

## 📊 Описание проекта

Набор данных содержит:
- Дату и время транзакции
- Способ оплаты (карта или наличные)
- Сумму покупки
- Название купленного кофе
- Анонимный ID клиента (по карте)
- Время суток (утро, день, вечер, ночь)

Цель проекта — визуализировать поведение клиентов и выявить ключевые тренды.

---

## 🛠️ Установка и запуск

### 1. Клонируй репозиторий

git clone https://github.com/remembermewho/coffee-sales-analysis

cd coffee-sales-analysis

### 2. Создай виртуальное окружение 

python -m venv .venv

### 3. Активируй окружение

Windows: .venv\Scripts\activate

Mac/Linux: source .venv/bin/activate

### 4. Установи зависимости

pip install -r requirements.txt

### 5. Получение данных 

Скачай Excel-файл с Kaggle:

https://www.kaggle.com/datasets/reignrichard/coffee-store-sales

Положи файл Coffe_sales.xlsx в папку data/ (создай её в корне проекта, если нет).

### 6. Запуск анализа

python coffee_analysis.py

### Графики сохранятся в папке /visuals (создай её в корне проекта, если нет).
