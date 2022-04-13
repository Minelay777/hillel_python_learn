'''Task 4. 10 points Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.
Пример(Example)
Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]
'''
my_list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
#сортируем и в качестве ключа используем лямбда функцию и передаём второй элемент
#кортежа - 1
my_list_sorted = sorted(my_list, key=lambda x: (x[1]))
print(my_list_sorted)