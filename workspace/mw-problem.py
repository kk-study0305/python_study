import random

home_number = 30000
man_number = 0
woman_number = 0
temp_check_number = 1
max_woman_number = 0
zero_woman_number = 0

for num in range(home_number):
    # 男が出るまで続ける
    man_check = False
    temp_man_number = 0
    temp_woman_number = 0
    while man_check == False:
        temp_check_number = random.randint(0, 9999) % 2
        # 0なら男、1なら女　男だったら
        if temp_check_number == 0:
            temp_man_number += 1
            man_number += 1
            man_check = True
            if temp_woman_number == 0:
                zero_woman_number += 1
        else:
            temp_woman_number += 1
            woman_number += 1
    if max_woman_number < temp_woman_number:
        max_woman_number = temp_woman_number
    # print('--------------------------------------------------------')
    # print(f'{num + 1}家庭目')
    # print(f'男は{temp_man_number}人、女は{temp_woman_number}人')

print(f'男は{man_number}人、女は{woman_number}人、男女比は{(man_number / woman_number)}')
print(f'もっとも女性が多い家庭には女性が{max_woman_number}人います。')
print(f'女性がいない家庭は{zero_woman_number}世帯です。')