"""
написать программу которая будет создавать список методов из доступных методов
питон объектов. Под доступными подразумевается методы без подчеркиваний. Фунции dir()
т.е для объекта set должен быть список методов
['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint',
 'issubset', 'issuperset', 'pop', 'remove', 'union', 'update']
"""
# берём список по dir(), и методом проверки на букву isalpha() добавляем
# только те, что без подчеркивания в новый список.

metod = dir(set)
new_list = []
for i in metod:
    if i.isalpha():
        new_list.append(i)
print(new_list)