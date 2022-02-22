"""
Task 1. 5 points
сложить словари в один.
использовать for и dict methods.
"""
#
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
#
dict_rezult1 = first | second | third | fourth | fifth
print("Складываем словари оператором | {}".format(dict_rezult1))

dict_rezult2 = {}
for key, value in first.items():
    dict_rezult2[key] = value
for key, value in second.items():
    dict_rezult2[key] = value
for key, value in third.items():
    dict_rezult2[key] = value
for key, value in fourth.items():
    dict_rezult2[key] = value
for key, value in fifth.items():
    dict_rezult2[key] = value
print("Складываем словари методом for {}".format(dict_rezult2))
