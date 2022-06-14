"""
1. Сделать примеры в файлике.
a) __call__
b) __repr__
c) @classmethod & @staticmethod
d) @property, setter, deleter
"""


# метод __call__

class Callee:
    def __call__(self, *args, **kwargs):
        print('Called: ', *args, **kwargs)


# метод __repr__

class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'выводим значения  {self.value}'


# метод @classmethod @staticmethod

class Coffee:

    def __init__(self, milk, beans):
        self.milk = milk
        self.coffee = 100 - milk
        self.beans = beans

    def __repr__(self):
        return f'Milk = {self.milk}% Coffee = {self.coffee}% Beans = {self.beans}'

    @classmethod
    def cappuchino(cls):
        return cls(80, 'Arrabika')

    @staticmethod
    def latte():
        return (95, 'Arrabika')


print(Coffee.cappuchino())
print(Coffee.latte())


# метод @property

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


if __name__ == '__main__':
    # метод __call__
    my_cal = Callee()
    my_cal(1, 2, 3, 4)

    # метод __repr__
    exemp = MyClass(4)
    print(exemp)

    # метод @classmethod @staticmethod
    print(Coffee.cappuchino())
    print(Coffee.latte())

    # метод @property
    bob = Person('Boby')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name

    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Person.name.__doc__)
