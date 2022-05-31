'''
Задача 3 30 баллов: написать функцию которая с помощью assert будет
 тестировать ваш самописный reduce
'''

my_list = [1, 2, 3, 4, 5, 6]


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
    my_var = 0
    for i in some_list:
        my_var = func(my_var, i)
    return my_var


def test_my_reduce():
    assert my_reduce(sum_func, my_list) == 21, 'popalsya'
    assert type(my_reduce(sum_func, my_list)) is int


if __name__ == '__main__':
    print(my_reduce(sum_func, my_list))
    print(type(my_reduce(sum_func, my_list)))

    test_my_reduce()
