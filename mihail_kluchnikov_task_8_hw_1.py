'''Task1. 5 points
Написать функцию которая будет принимать 3 аргумента (int)
 и находить максимум из них '''

a = 3
b = 4
c = 5

def max_of_three_arg(a, b, c):
    max_abc = max(a, b, c)
    print(f'Максимальное значение {max_abc}')
    return max_abc

max_of_three_arg(a, b, c)
