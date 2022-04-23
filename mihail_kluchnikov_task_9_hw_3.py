'''
Задача 3. 30 баллов
дописать декоратор, чтобы он принимал аргумент, например текст.
и выводил его тоже.

@methods_amount('need to learn')
[count, index]
'need to learn 2'
'''


def decor_func_count(text):
    def count_of_build_func(func):
        def wrapper(*args, **kwargs):
            print(f'{text}' + f' {len(func(*args, **kwargs))}')

        return wrapper

    return count_of_build_func


@decor_func_count('need to learn')
def show_all_nm_build_func(x):
    metod = dir(x)
    new_list = []
    for i in metod:
        if i.isalpha():
            new_list.append(i)
    print(new_list)
    return new_list


show_all_nm_build_func(list)
