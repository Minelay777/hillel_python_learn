'''
Задача 20 баллов написать функцию которая принимает от пользователя 2 аргумента
 и делит онин на другой. при попытке деления на ноль вывести пользователю
  "ай яй яй делить на ноль можно не многим"
Все остальные исключения с поймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"
'''

def func_of_segmentation(a: int, b: int)->int:
    print(a / b)

try:
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    func_of_segmentation(a, b)
except ZeroDivisionError:
    print("ай яй яй делить на ноль можно не многим")
except ValueError:
    print("надо вводить цифры, а не буквы")
finally:
    print(" I 'am happy that you learn python")
