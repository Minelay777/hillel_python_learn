"""
Задача_2. 5 баллов
Дан список с повторяющимися значениями необходимо из него удалить все
определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все 'eg'
Результат: ['bear', 'milk']
"""

some_list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
value = "eg"
while value in some_list:
    some_list.remove(value)  # Методом remove() удаляем нужный элемент
print(some_list)  # Печатаем очищенный список
