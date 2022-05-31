'''
Задача 4. 30 баллов: Создать класс с методом которого можно будет
возвращать область видимости созданного экземпляра класса.
В конструкторе(__init__) вашего класса пускай будут те параметры
которые вы захотите.
'''


class MyClass:
    def __init__(self, name):
        self.name = name

    def my_sum(sum1, sum2):
        """
        sum of sum1 and sum2
        :param sum1: int
        :param sum2: int
        :return: int
        """
        return sum1 + sum2

    def func_of_vizible(self):
        return dir(self)


my_example1 = MyClass
print(my_example1.my_sum(2, 3))
print(my_example1.func_of_vizible())

# print(dir(MyClass))
