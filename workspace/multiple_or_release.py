import time
import random

# 初期状態生成
init_life = 2500
shot_border = 50

player_a = init_life
player_b = init_life
player_c = init_life
player_d = init_life
player_a_living = 1
player_b_living = 1
player_c_living = 1
player_d_living = 1
ball_a = 1
ball_b = 1
ball_c = 1
ball_d = 1

# ターン


# Shotボーダー寄り小さければショット、大きければ倍増
# 
loop_number = 0
while player_a_living + player_b_living + player_c_living + player_d_living != 1 :
    dise_number_a = random.randint(0, 99)
    dise_number_b = random.randint(0, 99)
    dise_number_c = random.randint(0, 99)
    dise_number_d = random.randint(0, 99)
    
    time.sleep(1)
    loop_number += 1
    if loop_number % 5 == 0 and shot_border > 10:
        shot_border -= 1
        if shot_border % 10 == 0:
            print(f'Shot border is decreased. Now {shot_border}.')
    
    if dise_number_a >= shot_border and 0 < player_a:
        ball_a = ball_a * 2
        print(f'Now A balls = {ball_a}')
    elif dise_number_a < shot_border and 0 < player_a:
        print(f'Player A Shot! Release {ball_a} balls!')
        player_b = player_b - (ball_a // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_c = player_c - (ball_a // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_d = player_d - (ball_a // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_a = player_a + ball_a
        ball_a = 1
    elif 0 >= player_a:
        player_a_living = 0
        
    if dise_number_b >= shot_border and 0 < player_b:
        ball_b = ball_b * 2
        print(f'Now B balls = {ball_b}')
    elif dise_number_b < shot_border and 0 < player_b:
        print(f'Player B Shot! Release {ball_b} balls!')
        player_a = player_a - (ball_b // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_c = player_c - (ball_b // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_d = player_d - (ball_b // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_b = player_b + ball_b
        ball_b = 1
    elif 0 >= player_b:
        player_b_living = 0

    if dise_number_c >= shot_border and 0 < player_c:
        ball_c = ball_c * 2
        print(f'Now C balls = {ball_c}')
    elif dise_number_c < shot_border and 0 < player_c:
        print(f'Player C Shot! Release {ball_c} balls!')
        player_a = player_a - (ball_c // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_b = player_b - (ball_c // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_d = player_d - (ball_c // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_c = player_c + ball_c
        ball_c = 1
    elif 0 >= player_c:
        player_c_living = 0
        
    if dise_number_d >= shot_border and 0 < player_d:
        ball_d = ball_d * 2
        print(f'Now D balls = {ball_d}')
    elif dise_number_d < shot_border and 0 < player_d:
        print(f'Player D Shot! Release {ball_d} balls!')
        player_a = player_a - (ball_d // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_b = player_b - (ball_d // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_c = player_c - (ball_d // (player_a_living + player_b_living + player_c_living + player_d_living))
        player_d = player_d + ball_d
        ball_d = 1
    elif 0 >= player_d:
        player_d_living = 0
        
    print(f'-------------------------------------------------------------------------------------------')
    print(f'Now A life is {player_a}')
    print(f'Now B life is {player_b}')
    print(f'Now C life is {player_c}')
    print(f'Now D life is {player_d}')
    print(f'===========================================================================================')
    
    
# 勝者判別
if player_a_living == 1:
    print(f'Player A Win!')
elif player_b_living == 1:
    print(f'Player B Win!')
elif player_c_living == 1:
    print(f'Player C Win!')
elif player_d_living == 1:
    print(f'Player D Win!')