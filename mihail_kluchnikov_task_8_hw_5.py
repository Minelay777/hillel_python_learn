'''
30 points. познакомиться с модулем datetime и написать программу с помощью lambda
для возвращение текущего года, месяца , дня
например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))
'''

import datetime

now = datetime.datetime.now()
print(now)

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day

print(year(now))  # текущий год
print(month(now))  # текущий месяц
print(day(now))  # текущая дата дня месяца
