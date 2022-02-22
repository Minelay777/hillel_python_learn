"""
Task 5. 10 Вернуть из dictionary все уникальные values.
Пример:
Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}

Усложнение! +5 points
Вернуть ту же структуру.
После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]
"""

list_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# my_list = []
# list_dict2 = []
# for i in list_dict:
#     for k, v in i.items():
#         my_list.append(v)

my_list = [(k,v) for i in list_dict for k, v in i.items()]
#print(my_list)

my_list2 = list(map(lambda x: x[1], my_list))
print(my_list2)

# my_list3 = [j for i in my_list for j in i if ]
#
# print(my_list3)


#print(set(my_list))
#print(list_dict2)
