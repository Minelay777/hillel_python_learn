"""
Task 2. 10 points
1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
Пример:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15:
225}
2. просуммировать все значения(values), делается в одну строку.(look build in functions)
"""
# Генерируем словарь
dict_1 = {k: k * k for k in range(11, 21)}
print(dict_1)
# Считаем сумму всех values словаря
print('Сумма всех ключей словаря: {}'.format(sum(dict_1.values())))
