import os
import Process_game

os.system('cls')

type_game = input('Введите 1, если хотите играть с другим игроком, и любую другую цифру, если с ботом... ')
if (type_game == '1'):
    Process_game.player_vs_player()
else:
    intel = input('Введите 0, если хотите играть с глупым ботом, и любую другую цифру, если с умным... ')
    if intel == '0':
        Process_game.player_vs_stupid_bot ()
    else:
        Process_game.player_vs_smart_bot ()
