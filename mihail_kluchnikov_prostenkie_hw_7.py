"""
Для начала в одном файле.
1) 5 примеров list comprehension
2) 5 examples with DICT comprehension
3) 5 примеров с set comprehensions
"""

# list comprehension

cart = [3, 4, 12, 17, 19, 21, 23, 26, 30]
# создаём список из другого списка
cashier_2 = [item for item in cart]
print(cashier_2)
# создаём список только чётные значения
cashier_3 = [item for item in cart if item % 2 == 0]
print(cashier_3)
# создаём список только числа больше 100 и нечётные числа
cashier_4 = [item+100 for item in cart if item % 2 == 1]
print(cashier_4)
# создвём список из квадратов, на основе генератора
list_num = [x**2 for x in range(10)]
print(list_num)
# создвём список все цифры которого делятся на 5 без остатка, в диапазоне от 0 до 100
list_num2 = [x for x in range(100) if x%5 == 0]
print(list_num)

# DICT comprehension

# генератор словаря из генератора чисел
d = {a: a ** 2 for a in range(7)}
print(d)
# генератор словаря с квадратами значений ключа
c = {num: num**2 for num in range(1, 11)}
print(c)
# генератор нового словаря со всеми ключами в нижнем регистре
d1 = {'IOS': '15.4','IP': '10.255.0.1', 'hostname': 'london_r1', 'location': '21 New Globe Walk', 'model': '4451', 'vendor': 'Cisco'}
lower_d1 = {key.lower(): value for key, value in d1.items()}
# генератор нового словаря из двух списков
men = ['Bob', 'Frank', 'Pete']
women = ['Alice', 'Ann', 'Liz']
pairs = {w:m for w, m in zip(women, men)}
print(pairs)
# создание словаря из списка из чётных значений из списка
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {n: n ** 2 for n in nums if n % 2 == 0}
print(even_squares)

# set comprehensions

# генератор множества из списка
my_set = {s for s in [1, 2, 1, 0]}
print(my_set)
# генератор множества квадратов из списка
my_set2 = {s**2 for s in [1, 2, 1, 0]}
print(my_set)
# генератор множества квадратов из генератора чисел
my_set3 = {s**2 for s in range(10)}
# генератор множества квадратов из генератора чисел, только чётных значений
my_set4 = {s**2 for s in range(10) if s % 2 == 0}
# генератор множества только чисел из смешанного списка
vlans = [10, '30', 30, 10, '56']
unique_vlans = {int(vlan) for vlan in vlans}
print(unique_vlans)