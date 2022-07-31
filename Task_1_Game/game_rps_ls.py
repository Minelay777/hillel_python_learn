import random
"""
- создаём список вариантов
- создаём переменную со случайным значением взятым из списка вариантов
- запускаем цикл:
    -просим ввести фигуру из приведённого списка
    -после ввода игрока система сверяет введённую фигуру и случайную фигуру
    -выводит информацию кто выйграл
    -спрашивает: хочет игрок повторить или нет:
        если да - игра повторяется,
        если нет - программа завершается.
"""
variants: list = ['rock', 'paper', 'scissors', 'lizard', 'spok'] # список вариантов


while True:
    random_choice = random.choice(variants)  # случайный выбор машины
    player_choice: str = input('Your choice (rock paper scissors lizard spok)? ')

    if player_choice in variants:

        if player_choice == 'rock': # выбор игрока камень
            if random_choice == 'rock': # при совпадении выбра - ничья
                print('dead heat')
            elif random_choice == 'paper' or random_choice == 'spok':
                print('You LOSE')
            elif random_choice == 'scissors' or random_choice == 'lizard':
                print('You WIN')

        if player_choice == 'paper': # выбор игрока бумага
            if random_choice == 'paper':
                print('dead heat')
            elif random_choice == 'rock' or random_choice == 'scissors':
                print('You LOSE')
            elif random_choice == 'lizard' or random_choice == 'spok':
                print('You WIN')

        if player_choice == 'scissors': # выбор игрока ножницы
            if random_choice == 'scissors':
                print('dead heat')
            elif random_choice == 'rock' or random_choice == 'spok':
                print('You LOSE')
            elif random_choice == 'paper' or random_choice == 'lizard':
                print('You WIN')

        if player_choice == 'lizard': # выбор игрока ящерица
            if random_choice == 'lizard':
                print('dead heat')
            elif random_choice == 'rock' or random_choice == 'scissors':
                print('You LOSE')
            elif random_choice == 'paper' or random_choice == 'spok':
                print('You WIN')

        if player_choice == 'spok': # выбор игрока Спок
            if random_choice == 'spok':
                print('dead head')
            elif random_choice == 'paper' or random_choice == 'lizard':
                print('You LOSE')
            elif random_choice == 'rock' or random_choice == 'scissors':
                print('You WIN')
    else:
        print(f'Invalid input {player_choice}')  # если игрок ввёл некорректные данные выводим сообщение
    player_continue_choice = input('Do you want to continue: y or n: ')  # спрашиваем, хочет ли игрок продолжить или закончить
    if player_continue_choice == 'n':
        break