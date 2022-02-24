"""
сделать пример функции
    без return c pass or ...
    сделать 5 различных функций на свое усмотрение.
"""


def sum_arguments(x, y):
    print(x + y)


def square_of_value(x):
    print(x ** 2)


def сongratulations_on_the_holiday(name):
    print('Поздравляю с прздниками товарищь {}'.format(name))


def generate_list_number(x):
    numbers = list(range(x))
    print(numbers)


def generate_list_of_squares(x):
    list_num = [x ** 2 for x in range(10)]
    print(list_num)
