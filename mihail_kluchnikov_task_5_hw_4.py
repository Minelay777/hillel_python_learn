"""
Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.

Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.

Входные данные: red, white, black, red, green, black
Результат: black, green, red, white
"""

# Вводим данные
us = input("Введите несколько слов через запятую: ")
# создаём список методом split()
ul = us.split(", ")
# удаляем повторяющиеся значения
ul2 = list(set(ul))
# сортируем наш список
ul2.sort()
# сшиваем список в строку
us2 = ", ".join(ul2)
# выводим на печать нашу новую строку
print(us2)
