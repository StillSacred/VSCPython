# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)

#coding: utf8
#Крестики нолики
#Компьютер играет в крестики -нолики против пользователя
#глобальные константы
X="X"
O="O"
EMPTY=' '
TIE="Ничья"
NUM_SQUARES=9

def display_instruct():
    '''Выводит на экран иснтрукцию для игрока'''
    print(
"""
Добро пожаловать в игру Крестики-нолики!
С Вами будет сражаться компьютер.
Чтобы сделать свой ход, введите от 0 до 8.
Числа соответсвуют полям доски:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
Приготовься к игре, Противник, сейчас начнется решающее сражение!\n
"""
        )
def ask_yes_no(question):
    """Задает вопросы с ответом 'Да' или'Нет".    """
    response=None
    while response not in("y","n"):
        response=input(question).lower()
    return response
def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response
def pieces():
    "Определяет принадлежность первого хода"
    go_first=ask_yes_no("Хочешь оставить за собой первый ход?(y/n): ")
    if go_first=="y":
        print ("\n Ну что ж, даю Тебе фору - играй крестиками")
        human = X
        computer = O
    else:
        print("\n Спасибо за то, что предоставил перове право хода компьютеру")
        computer = X
        human = O
    return computer, human
def new_board():
    "Создает новую игровую доску"
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
def  display_board(board):
    """Отображает игровую доску на экране."""
    print("\n\t", board[0], "|", board[1],"|",board[2])
    print("\t",  "---------")
    print("\n\t", board[3], "|", board[4],  "|", board[5])
    print("\t",  "---------")
    print("\n\t", board[6], "|", board[7],  "|",  board[8],"\n")

def legal_moves(board):
    """Создает список доступных ходов """
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
def winner(board):
    """Определяет победителя в игре """
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]] !=EMPTY:
            winner=board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board,human):
    """ Получает ход человека"""
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_number("Твой ход. Выбери одно из полей (0-8):",0, NUM_SQUARES)
        if move not in legal:
            print ("\nСмешной человек! Это поле уже занято. Выбери другое.\n")
    print("Хорошо.....")
    return move
def computer_move(board, computer, human):
    """Делает ход копмьютер """
    #создание рабочей копии доски, потому что функция будет менятьнекоторые значения вс писке
    board=board[:]
    #поля от лучшего к худшему
    BEST_MOVES=[4,0,2,6,8,1,3,5,7]
    print("Я выберу номер", end=" ")
    for move in legal_moves(board):
        board[move]=computer
        #Если следующим хододом может победитькомпьютер,выберем тогда ход
        if winner(board)==computer:
            print(move)
            return move
        #выполним проверку, отменим внесения изменения
        board[move]=EMPTY
    #  поскольку следующим ходом  ни  одна  сторона  не  может  победить.
    #  выберем лучшее из  доступных  полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):
    """Осуществляет переход хода."""
    if turn==X:
        return O
    else:
        return X
def congrat_winner(the_winner, computer, human):
    """Поздравляем победителя игры."""
    if the_winner !=TIE:
        print("Три",the_winner,"в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победил компьютер!")
    elif the_winner==human:
        print("Поздравляю, Вы победили компьютер!")
    elif the_winner==TIE:
        print("Ничья!")
def main():
    """Основная часть программы """
    display_instruct()
    computer, human =pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn ==human:
            move=human_move(board,human)
            board[move]=human
        else:
            move=computer_move(board,computer,human)
            board[move]=computer
        display_board(board)
        turn = next_turn(turn)
    the_winner=winner(board)
    congrat_winner(the_winner,computer,human)

#Запуск программы
main()
input("\n\nНажмите Enter, чтобы выйти.")