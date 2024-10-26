# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# - можно также попробовать рассчитать IQR
# 6. Вычислите стандартное отклонение


import pandas as pd

# Задача 1
data = {
    'student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Denis', 'Felix', 'Gloria', 'Helen', 'Ivan'],
    'Math': [5, 4, 3, 5, 4, 2, 5, 4, 3, 5],
    'History': [4, 5, 3, 4, 5, 5, 4, 3, 5, 2],
    'Geography': [3, 4, 4, 5, 5, 3, 2, 5, 4, 3],
    'Physics': [5, 4, 3, 4, 2, 5, 4, 5, 4, 5],
    'Chemistry': [4, 5, 3, 4, 5, 3, 4, 4, 5, 5]
}
df = pd.DataFrame(data)

# Задача 2
print(df.head())

# Задача 3
for lesson in df.columns:
    if lesson != 'student':
        print(f"Средняя оценка по {lesson} - {df[lesson].mean()}")

# Задача 4
for lesson in df.columns:
    if lesson != 'student':
        print(f"Медианная оценка по {lesson} - {df[lesson].median()}")

# Задача 5
Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
print(f"Q1_math - {Q1_math}")
print(f"Q3_math - {Q3_math}")
print(f"IQR - {Q3_math - Q1_math}")

# Задача 6
for lesson in df.columns:
    if lesson != 'student':
        print(f"Стандартное отклонение по {lesson} - {df[lesson].std()}")
