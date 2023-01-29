import random

check_count = 0
is_check = False
while is_check == False:
    print(f'{check_count + 1}回目のテストです')
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    sum = a + b
    c = int(input(f'{a}+{b}=>>>'))
    if sum == c:
        print('正解です')
        is_check = True
    else:
        print('不正解です')
        is_check = False
        check_count += 1
print(f'あなたは正解するのに{check_count + 1}回かかりました。')