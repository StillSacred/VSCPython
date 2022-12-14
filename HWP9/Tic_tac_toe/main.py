# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# ( можно любую задачу, главное файл с библиотекой чтобы был в формате тхт).

from emoji import emojize as em
from random import randint

x = em(':x:', language='alias')
o = em(':o:', language='alias')

def check_input(data: str):
    while not data.isdigit() or not 1 <= int(data) <=9:
        data = input('Введено неверное значение. Повторите ввод\n')
    return data

def another_round():
    if input('Хотите сыграть еще? да / нет\n') == 'да':
        return True
    else:
        return False

def show_field(arr):
    print(f' {arr[0]} | {arr[1]} | {arr[2]}')
    print('='*13)
    print(f' {arr[3]} | {arr[4]} | {arr[5]}')
    print('='*13)
    print(f' {arr[6]} | {arr[7]} | {arr[8]}')
    print()

def check_field(arr):
    if arr[0] == x and arr[1] == x and arr[2] == x:
        return True
    elif arr[3] == x and arr[4] == x and arr[5] == x:
        return True
    elif arr[6] == x and arr[7] == x and arr[8] == x:
        return True
    elif arr[0] == x and arr[3] == x and arr[6] == x:
        return True
    elif arr[1] == x and arr[4] == x and arr[7] == x:
        return True
    elif arr[2] == x and arr[5] == x and arr[8] == x:
        return True
    elif arr[0] == x and arr[4] == x and arr[8] == x:
        return True
    elif arr[2] == x and arr[4] == x and arr[6] == x:
        return True
    elif arr[0] == o and arr[1] == o and arr[2] == o:
        return True
    elif arr[3] == o and arr[4] == o and arr[5] == o:
        return True
    elif arr[6] == o and arr[7] == o and arr[8] == o:
        return True
    elif arr[0] == o and arr[3] == o and arr[6] == o:
        return True
    elif arr[1] == o and arr[4] == o and arr[7] == o:
        return True
    elif arr[2] == o and arr[5] == o and arr[8] == o:
        return True
    elif arr[0] == o and arr[4] == o and arr[8] == o:
        return True
    elif arr[2] == o and arr[4] == o and arr[6] == o:
        return True
    else:
        return False

game_is_on = True
while game_is_on:
    cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    free_cells = 9
    print('Добро пожаловать в игру "Крестики-нолики"!\n')
    game_mode = input('Выберите режим игры: 1 - игрок против игрока, 2 - игрок против компьютера\nexit - выход из игры\n').lower()
    if game_mode == '1':
        print('Выбран режим "Игрок против Игрока".\nИгрок 1 - крестики. Игрок 2 - нолики.\n')
        coin = randint(1,2)
        if coin == 1:
            player1 = True
        else:
            player1 = False
        finish = False
        while not free_cells == 0 and not finish:
            if player1:
                print('Игрок 1, Ваш ход\n')
                show_field(cells)
                move = int(check_input(input('Выберите ячейку\n')))
                while cells[move-1] == x or cells[move-1] == o:
                    move = int(check_input(input('Эта ячейка уже занята! Выберите другую\n')))
                cells[move-1] = x
                player1 = False
                free_cells -= 1
                finish = check_field(cells)
            else:
                print('Игрок 2 Ваш ход\n')
                show_field(cells)
                move = int(check_input(input('Выберите ячейку\n')))
                while cells[move-1] == x or cells[move-1] == o:
                    move = int(check_input(input('Эта ячейка уже занята! Выберите другую\n')))
                cells[move-1] = o
                player1 = True
                free_cells -= 1
                finish = check_field(cells)
        show_field(cells)
        if free_cells == 0:
            print('Ничья!')
            game_is_on = another_round()
        elif player1:
            print('Выиграл Игрок 2!')
            game_is_on = another_round()
        else:
            print('Выиграл Игрок 1!')
            game_is_on = another_round()
    if game_mode == '2':
        print('Выбран режим "Игрок против Компьютера".\nИгрок - крестики. Компьютер - нолики.\n')
        coin = randint(1,2)
        if coin == 1:
            player = True
        else:
            player = False
        finish = False
        while not free_cells == 0 and not finish:
            if player:
                print('Игрок 1, Ваш ход\n')
                show_field(cells)
                move = int(check_input(input('Выберите ячейку\n')))
                while cells[move-1] == x or cells[move-1] == o:
                    move = int(check_input(input('Эта ячейка уже занята! Выберите другую\n')))
                cells[move-1] = x
                player = False
                free_cells -= 1
                finish = check_field(cells)
            else:
                move = randint(0, len(cells)-1)
                while cells[move] == x or cells[move] == o:
                    move = randint(0, len(cells)-1)
                cells[move] = o
                player = True
                free_cells -= 1
                print('Компьютер делает ход\n')
                show_field(cells)
                finish = check_field(cells)
        show_field(cells)
        if free_cells == 0:
            print('Ничья!')
            game_is_on = another_round()
        elif player:
            print('Выиграл Компьютер!')
            game_is_on = another_round()
        else:
            print('Выиграл Игрок!')
            game_is_on = another_round()

    if game_mode == 'exit':
        print('До свидания!')
        game_is_on = False