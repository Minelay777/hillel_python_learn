'''
Задача повышенной Интересности. Попробовать посмотреть на написанный код
 и сделать его более надежным. Любые изменения приветствуются.
просмотреть каждую программу и посмотреть как она может упасть.
Попробовать ее зафейлить.
Во время тестирования заметить какие ошибки появляется
используя исключения изменить код. И не только исключения, а и фантазию.

def example1():
    for i in range(3):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', x / y)


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        sumOfPairs.append(L[i] + L[i + 1])

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example3([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")

main()
'''

'''в этом блоке надо перехватить деление на ноль и заменить нолль на 1 или предложить повторный ввод, но как я не разобрался ('''
def example1():
    for i in range(3):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', x / y)


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        sumOfPairs.append(L[i] + L[i + 1])

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example3([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")

try:
    main()
except ZeroDivisionError:
    print('на ноль делить нельзя')
except ValueError:
    print('надо вводить только цифры')