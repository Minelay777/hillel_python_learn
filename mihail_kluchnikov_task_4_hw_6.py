"""
Task 4.15 Удалить дубликаты из dictionary, пример
Before :
{'id1':{'name': 'Ruslan', 'class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark', 'class': 2, 'subjects' : {'Geometry', 'Java', 'Cooking'}},
'id3':{'name': 'Ruslan', 'class': 1, 'subjects' : {'Math', 'Algorithms', 'English'}}}
After:
{'id1':{'name': 'Ruslan', 'class': 1, 'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark', 'class': 2, 'subjects' : {'Geometry', 'Java', 'Cooking'}}
"""

dict1 = {
    'id1': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}},
    'id2': {'name': 'Mark', 'class': 2, 'subjects': {'Geometry', 'Java', 'Cooking'}},
    'id3': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}
}

dict2 = {}
for key, value in dict1.items():  # Проходим по первому словарю
    if value not in dict2.values():  # Проверяем отсутвие совпадения всех values во 2 словаре и тогда
        dict2[key] = value  # добавляем в 2 словарь значение из первого словаря.
print(dict2)
