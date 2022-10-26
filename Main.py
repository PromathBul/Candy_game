from random import randint
import Methods

candies = 2021
max_move = 28
count_for_check_win = candies // max_move

name_player = input('Введите свое имя: ')

determing_moves = randint(0, 1)

win = False
while not win:
    if determing_moves % 2 == 0:
        candies = Methods.move_player(name_player, candies, max_move)
    else:
        candies = Methods.move_bot(candies, max_move)
    if determing_moves >= count_for_check_win - 1:
        temp = Methods.check_win(candies, determing_moves, name_player)
        if temp:
            print(f'{temp} выиграл')
            win = True
    determing_moves += 1