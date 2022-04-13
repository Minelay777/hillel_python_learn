'''Task2. 10 points
Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя  функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента и находить максимум с помощью функции1.
в итоге будет псевдокод:

функция_нахождения_макс_из_2х(арг1, арг2):
    return максимальное значение из 2х аргументов

функция_нахождения_макс_из_3х(арг1, арг2, арг3):
	использую тут функция_нахождения_макс_из_2х()
    return максимальное значение из 3х аргументов.
def finding_max_tw(one, two):
    pass

def finding_max_three(one, two, three):
    middle = finding_max_tw(one, two)
    return finding_max_tw(middle, three)
'''

one = 1
two = 2
three = 3

def finding_max_tw(one, two):
    return max(one, two)

def finding_max_three(one, two, three):
    middle = finding_max_tw(one, two)
    return finding_max_tw(middle, three)

print(finding_max_three(one,two,three))