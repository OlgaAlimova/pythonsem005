# Создайте программу для игры в ""Крестики-нолики""

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_table(sm_list):
    print(f'{sm_list[0]} | {sm_list[1]} | {sm_list[2]}')
    print('-----------')
    print(f'{sm_list[3]} | {sm_list[4]} | {sm_list[5]}')
    print('-----------')
    print(f'{sm_list[6]} | {sm_list[7]} | {sm_list[8]}')
    print('-----------')


print('Сыграем? Вот поле: ')
print()
print_table(field)
print()
print('Я пожалуй начну. Чтобы сделать ход, вводи цифру поля, '
      'в которую хочешь поставить нолик')

import random

def won(n):
    won_res = 0
    if field[0] == n and field[1] == n and field[2] == n:
        won_res = 1
    if field[3] == n and field[4] == n and field[5] == n:
        won_res = 1
    if field[6] == n and field[7] == n and field[8] == n:
        won_res = 1
    if field[0] == n and field[3] == n and field[6] == n:
        won_res = 1
    if field[1] == n and field[4] == n and field[7] == n:
        won_res = 1
    if field[2] == n and field[5] == n and field[8] == n:
        won_res = 1
    if field[0] == n and field[4] == n and field[8] == n:
        won_res = 1
    if field[2] == n and field[4] == n and field[6] == n:
        won_res = 1
    if won_res == 1:
            print(f'Поздравляю! "{n}" выиграли')
    return won_res

def checking_value_bot(list1):
    occupied = False
    while not occupied:
        bot_step = random.randint(1, 9)
        if str(list1[bot_step - 1]) not in 'X0':
            print(f'Я выбираю поле {list1[bot_step - 1]}')
            print()
            occupied = True
        else:
            print('Так, эта клеточка занята. Тогда я схожу сюда...')
    return bot_step

def checking_value_player(list2):
    occupied = False
    while not occupied:
        player_step = int(input('Ваш ход: '))
        if player_step >= 1 and player_step <= 9:
            if str(list2[player_step - 1]) not in 'X0':
                occupied = True
                print('Принято')
            else:
                print('Это поле занято. Введите номер свободного поля')
        else:
            player_step = int(input('Некорректное число. Введите число от 1 до 9: '))
    return player_step



for i in range(10):
    my_move = checking_value_bot(field)
    field[my_move - 1] = 'X'
    print_table(field)

    temp = field[my_move - 1]
    if won(temp) == 1:
        break

    turn = checking_value_player(field)
    field[turn - 1] = '0'
    print_table(field)

    temp = field[turn - 1]
    if won(temp) == 1:
        break
    if i == 9:
        break

