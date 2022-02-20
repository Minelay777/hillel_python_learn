"""
Задача 9. 10 баллов
Тема Листы
Даны два списка элементов если хоть один елемент совпадает отпринтить True.
print(Тrue) не слово! а объект подставить.
"""
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

if x1.intersection(x2):
	print("множества x1 и x2 пересекаются элементом: {}".format(x1.intersection(x2)))
else:
	print("не пересекаются")

#result = []
result = list(set(x1) & set(x2))
if result:
	 print("множества x1 и x2 пересекаются элементом: {}".format(result))
else:
	print("не пересекаются")
