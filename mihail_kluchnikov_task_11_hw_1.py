'''
Задача 1. 10 баллов, написать 3 примера генераторных функций
 с различными последовательностями.
'''


def gensquares(n: int) -> int:
    '''
    return squares of n
    :param n: int
    :return: generator
    '''
    for i in range(n):
        yield i ** 2


def step_by_step() -> str:
    yield 'шаг'
    yield 'ещё шаг'
    yield 'ещё шажочек'
    yield 'вот мы и пришли'


def geometric_progression(n: int) -> int:
    '''
    function generate geometric progression
    :param n: int
    :return: generator
    '''
    for x in range(n):
        yield x * (x + 1)


if __name__ == '__main__':

    for i in gensquares(5):
        print(i)

    for i in step_by_step():
        print(i)

    for i in geometric_progression(3):
        print(i)
