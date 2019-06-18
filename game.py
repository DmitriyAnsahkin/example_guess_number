import random

from functions import game, read_input_continue_game

hidden_number = random.randrange(0, 100)                # имена переменных должны нести логический смысл
continue_flag = True                                    # флаги тоже выносим в начало

while continue_flag:

    # несколько вариантов построения игры. Можно раскоменчивать/закоменчивать и пробовать разные варианты

    # game()                                            # это будет просто игрой по-умолчанию
    # game(counter=5)                                   # это будет игрой с 5-ью попытками вместо трех
    game(counter=10, hidden_number=hidden_number)       # а это будет игра с числом от 0 до 99 с 10 попытками

    response = read_input_continue_game()

    if response == 'n':
        continue_flag = False
        print('Спасибо за игру')
