"""
Задача_3. 10 баллов
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even"
если все четные и NO если нет.
Пример входных данных: [11, 23, 65, 44, 76, 533]
Результат: NO
Пример входных данных: [12, 22, 66, 44, 76, 534]
Результат: all numbers are even
"""
my_list1 = [11, 23, 65, 44, 76, 533]
my_list2 = [12, 22, 66, 44, 76, 533]

counter = 0  # Счётчик
# Используя счётчик, обращаемся к элементам списка и проверяем на не чётность. И если нечётное - выводим "NO" и конец.
while counter < len(my_list1):
    if (my_list1[counter] % 2) != 0:
        print("NO")
        break
    counter += 1
else:  # Если все чётные, то мы попадаем сюда.
    print("all numbers are even")
