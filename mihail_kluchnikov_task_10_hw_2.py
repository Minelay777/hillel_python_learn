'''
2. Скинуть файлик с примерами всех конструкций КРОМЕ менеджера
 контекста. With/as. 20 баллов
'''

def fetcher(obj, index):
    return obj[index]

x = 'spam'
print(fetcher(x, 3))

# выведем 4 по счёту символ, которого нет
# перехватим ошибку методом try/except
try:
    print(fetcher(x, 4))
except IndexError:
    print('got exception')

def catcher():
    try:
        print(fetcher(x, 4))
    except IndexError:
        print('got exception in catcher')
    print('continuing')

catcher()

# принудительно создадим исключение
# методом try/raise и перехватим его методом try/except

try:
    raise IndexError
except IndexError:
    print('got exception from raise')


# перехват исключений методом try/finally
# выполнение блока кода после появления исключения

try:
    fetcher(x, 4)
finally:
    print('after fetch')

# принудительное создание исключения
# методом assert

assert False, 'Nobody expect the Spanish Inquisition!'
