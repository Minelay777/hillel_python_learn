"""
Задача_6 5 балллов
Написать примеры всех методов из set объекта.
"""
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])
# copy
new_set = set1.copy()
# discard(x)
set1.discard(3)
# remove()
set1.remove(3)
# union()
set2 = {5, 6, 7}
set1.union(set2)
# x.update(y, z)
set3 = {8, 9, 10}
set1.update(set2, set3)
# pop()
set1.pop()
# clear()
set1.clear()
# x.difference(y)
set1.difference(set2)
# x.difference_update(y)
set1.difference_update(set2)
# x.intersection(y)
set1.intersection(set2)
# intersection_update(y)
set1.intersection_update(set2)
# x.symmetric_difference(y)
set1.symmetric_difference(set3)
# symmetric_difference_update()
set1.symmetric_difference_update(set3)