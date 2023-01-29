import random
import time

gacha_list = []
gacha_number = 100
try_number = 0

# ガチャの大本の生成
for i in range(gacha_number):
    gacha_list.append(i)
# 自分の所持数一覧
my_item_list = []
for i in range(gacha_number):
    my_item_list.append(0)

complate_check = False
while complate_check == False:
    try_number += 1 
    # time.sleep(1)
    x = random.randint(0, 99)
    print(f'You {x} get!')
    my_item_list[x] += 1
    if all(my_item_list):
        complate_check = True
    print(my_item_list)

print(f'コンプまで{try_number}回')
print(f'最大{max(my_item_list)}個')