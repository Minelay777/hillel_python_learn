'''
Задача 2 10 баллов: написать свою реализацию функции reduce() с описанием
 в инлайновых и многострочных комментариях ее работы.
def my_reduce(): моя реализация. (постарайтесь по памяти реализовать.)
'''

my_list = [1, 2, 3, 4, 5]


def sum_func(one, two):
    '''
    function sums two variables
    :param one: int
    :param two: int
    :return: int
    '''
    return one + two


def my_reduce(func, some_list):
    '''
    my realization of standart function - rezult()
    :param func: some function
    :param some_list: iterable object
    :return: rezult of 'some function' + 'itrable objeect'
    '''
    my_var = 0  # создаём переменную, которая будет накапливать значения
    for i in some_list:  # перебираем список со значениями
        my_var = func(my_var, i)  # накапливаем в переменной результат работы функции с переданным значением из списка
    print(my_var)  # выводим накопленый результат из переменной в консоль


if __name__ == '__main__':

    my_reduce(sum_func, my_list)
