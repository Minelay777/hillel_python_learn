"""
Task3. 5 points
отсортировать словарь по ключам
"""
# Берём некий словарь
d = {'b': 9, 'a': 3, 'c': 7}
# Превращаем словарь в кортеж, сортируем кортеж, отсортированный кортеж превращаем в новый словарь
d_s = dict(sorted(d.items()))
print('Наш новый отсортированный словарь: {}'.format(d_s))
