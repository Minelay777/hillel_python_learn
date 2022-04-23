'''
Задача 2. 20 баллов
Написать функцию которая будет у пользователя брать python обект в любом виде
и выводить все его не магические методы в списке.
и написать декторатор который будет выводить колличество методов в объекте.

Похожую задачу мы уже решали. Можете взять решение из предыдущей .
Но декоратор уже ваш полностью)
func(tuple())
[count, index]

@methods_amount
[count, index]
2
'''


def count_of_build_func(func):
    def wrapper(*args, **kwargs):
        print(len(func(*args, **kwargs)))

    return wrapper


@count_of_build_func
def show_all_nm_build_func(x):
    metod = dir(x)
    new_list = []
    for i in metod:
        if i.isalpha():
            new_list.append(i)
    print(new_list)
    return new_list


show_all_nm_build_func(list)
