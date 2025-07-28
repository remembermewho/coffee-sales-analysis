import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка
df = pd.read_excel('data/Coffe_sales.xlsx')

# Преобразования
df['datetime'] = pd.to_datetime(df['datetime'])
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()
df['hour'] = df['datetime'].dt.hour
df['month'] = df['date'].dt.to_period('M').astype(str)

# Прибыль по дням недели
def plot_sales_by_day():
    dow = df.groupby('day_of_week')['money'].sum().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )
    dow.plot(kind='bar', title='Доход по дням недели (в южноафриканских рэндах)')
    plt.tight_layout()
    plt.savefig('visuals/sales_by_day.png')
    plt.close()

# Популярные кофе
def plot_coffee_types():
    top_coffee = df['coffee_name'].value_counts().head(5)
    sns.barplot(x=top_coffee.values, y=top_coffee.index)
    plt.title("Top 5 Types of Coffee")
    plt.tight_layout()
    plt.savefig('visuals/top_coffee.png')
    plt.close()
    


# Продажи по времени суток (по столбцу Time_of_Day)
def plot_sales_by_time_of_day():
    # Группируем по Time_of_Day и считаем сумму money
    sales = df.groupby('Time_of_Day')['money'].sum().reindex(['Morning', 'Afternoon', 'Night'])

    ax = sales.plot(kind='bar', title='Продажи по времени суток', figsize=(8,5), color='skyblue')

    # Подписи значений сверху на столбиках
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

    plt.xlabel('Время суток')
    plt.ylabel('Сумма продаж (ZAR)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('visuals/sales_by_time_of_day.png')
    plt.close()

# Подсчет прибыли по месяцам
def plot_sales_by_month():
    df['month'] = df['date'].dt.to_period('M').astype(str)
    monthly_sales = df.groupby('month')['money'].sum()

    # Создаем график и получаем объект оси
    ax = monthly_sales.plot(kind='bar', title='Прибыль по месяцам', figsize=(10, 5))
    plt.xlabel('Месяц')
    plt.ylabel('Прибыль (ZAR)')
    plt.xticks(rotation=45)
    
    # Добавляем значения на столбики
    for patch in ax.patches:
        height = patch.get_height()
        ax.text(
            x=patch.get_x() + patch.get_width() / 2,  # позиция по X (центр столбика)
            y=height + 0.01 * max(monthly_sales),     # позиция по Y (немного выше вершины)
            s=f'{height:,.0f}',                       # форматированное значение
            ha='center',                              # горизонтальное выравнивание
            va='bottom',                              # вертикальное выравнивание
            fontsize=9
        )
    
    plt.tight_layout()
    plt.savefig('visuals/sales_by_month.png')
    plt.close()

# Запуск
if __name__ == "__main__":
    plot_sales_by_day()
    plot_coffee_types()
    # plot_sales_by_day_time()
    plot_sales_by_time_of_day()
    plot_sales_by_month()
    print("Графики сохранены в папке visuals/")
