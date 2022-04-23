'''
Задача 4. 30 баллов
Ваша задача - создать декоратор для функции, которая принимает неограниченное
количество позиционных ХЕШИРУЕМЫХ элементов.
Декоратор добавляет следующий функционал:
Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть
результат выполнения этой функции из памяти, а не вычислять его заного.
Если не вызывалась - вычислить результат, положить его в память, и вернуть.
Подсказка - тут вам пригодятся словари.
'''


def decorator(func):
    cashe_dict = {}

    def wrapper(*args):
        if args is cashe_dict:
            return cashe_dict[args]
        else:
            answer = func(*args)
            cashe_dict[args] = answer
        return answer

    return wrapper


@decorator
def func_of_sum(*args):
    return sum(args)


print(func_of_sum(1, 2, 3, 4))
print(func_of_sum(1, 2, 3, 4))
print(func_of_sum(1, 2, 3, 4, 5))
