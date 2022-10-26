from random import randint

def move_player(name_player, candies, max_move):
    valid = False
    while not valid:
        move = input(f'{name_player}, Ваш ход... ')
        try:
            move = int(move)
            if move > 0 and move <= max_move and move <= candies:
                print(f'Вы забрали {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                valid = True
            else:
                print('Количество взятых конфет должно быть в интервале от 1 до 28 или не больше оставшегося количества конфет')
        except:
            print('Необходимо ввести целое число.')
    return candies

def move_bot(candies, max_move):
    move = candies % (max_move + 1)
    if move == 0:
        move = randint(1, max_move)
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

def check_win(candies, determing_moves, name):
    if candies == 0:
        return name if determing_moves % 2 == 0 else 'Бот'
    else:
        return False

candies = 2021
max_move = 28
count_for_check_win = candies // max_move

name_player = input('Введите свое имя: ')

determing_moves = randint(0, 1)

win = False
while not win:
    if determing_moves % 2 == 0:
        candies = move_player(name_player, candies, max_move)
    else:
        candies = move_bot(candies, max_move)
    if determing_moves >= count_for_check_win - 1:
        temp = check_win(candies, determing_moves, name_player)
        if temp:
            print(f'{temp} выиграл')
            win = True
    determing_moves += 1