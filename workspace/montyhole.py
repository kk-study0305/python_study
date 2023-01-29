import random
#初期設定
#1番が当たり
roop_number = 1000
success = 0
faild = 0
door_chenge = 1

if door_chenge == 1:
    print('ドアを変更します。')
else:
    print('ドアを変更しません。')
for num in range(roop_number):
    array = [0, 0, 0]
    correct_number = random.randrange(0,3)
    array[correct_number] = 1

    #自分が選んだ扉
    select_number = random.randrange(0,3)
    #司会者が選ぶ扉
    for num_chair in range(3):
        if num_chair != correct_number and num_chair != select_number:
            chair_number = num_chair
            break    
    #変える場合
    if door_chenge == 1:
        #チェンジ
        for num_change in range(3):
            if select_number != num_change and chair_number != num_change:
                select_number = num_change
                break
        #正誤判定
        if array[select_number] == 1:
            success += 1
        else:
            faild += 1
    #変えない場合
    else:
        if array[select_number] == 1:
            success += 1
        else:
            faild += 1

#結果
print(f'正解数: {success} 失敗数: {faild}')
print(f'正解率: {round((success / roop_number) * 100,2)}%, 不正解率: {round((faild / roop_number) * 100,2)}%')
    