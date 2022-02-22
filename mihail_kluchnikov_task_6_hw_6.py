"""
Task 6. 15 Посчитать общее количество наименований в списке. И только в списках.
Example:
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
Результат: 6
"""
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'],
           'thuesday': None,
           'wednesday': ['manicure', 'hammam', 'beer']
           }
k = 0
for key, value in shedule.items():
    if value == None:  # Чтобы не выводило ошибку вставляем continue
        continue
    k += len(value)  # Прибавляем к k длину списка из value нашего словаря
print('Общее количество наименований в списке {}'.format(k))
