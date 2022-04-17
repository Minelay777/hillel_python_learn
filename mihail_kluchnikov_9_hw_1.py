'''
Задача 1. 10 баллов
Написать функцию которая будет добовлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции.
my_number = user_telephone('+044')
my_number('838372893')
+044838372893 результат.
'''

def my_number(number):
    def user_telephone():
        print('+044' + number)
    return user_telephone
f = my_number('838372893')
f()