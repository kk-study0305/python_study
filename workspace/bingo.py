import random
import time

# ビンゴ生成
row_1st = []
row_2nd = []
row_3rd = []
row_4th = []
row_5th = []
bingo_list_raw = [
                row_1st, 
                row_2nd,
                row_3rd,
                row_4th,
                row_5th
                ]
bingo_list = []

# ルーレット生成
roulette = []
for i in range(75):
    roulette.append(i + 1)


# 数字挿入
for i in range(5):
    while len(bingo_list_raw[i]) < 5:
        n = random.randint((15 * i + 1), (15 * (i + 1)))
        if not n in bingo_list_raw[i]:
            bingo_list_raw[i].append(n)

# 行と列の入れ替え
for i in range(5):
    row_tmp = [bingo_list_raw[0][i],bingo_list_raw[1][i],bingo_list_raw[2][i],bingo_list_raw[3][i],bingo_list_raw[4][i]]
    bingo_list.append(row_tmp)
# 中央をfreeにして完成
bingo_list[2][2] = 0

# チェック用二次元リスト
check_list = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]   
]

# 縦横斜めのどれかが0のみになるまで継続
check_bingo = False
check_column = []
while check_bingo == False:
    time.sleep(2)
    for i in bingo_list:
        print(i)
    # 抽選
    roulette_num = roulette.pop(random.randint(1,len(roulette)) - 1)
    print(f'{roulette_num}がでました。')
    # 抽選した数字がシートのどこにあるかチェック
    for x in range(5):
        for y in range(5):
            if bingo_list[x][y] == roulette_num:
                print(f'あたり！')
                check_list[x][y] = 1
    print("現在の状況")
    for i in check_list:
        print(i)
    
    # 横のチェック
    for i in range(5):
        if all(check_list[i]) == True:
            check_bingo = True
    # 縦のチェック
    # チェック用配列生成してからチェック
    for i in range(5):
        check_column = [check_list[0][i],check_list[1][i],check_list[2][i],check_list[3][i],check_list[4][i]]
        if all(check_column) == True:
            check_bingo = True
    # 斜めのチェック
    # チェック用配列生成してからチェック
    check_diag_1 = [check_list[0][0],check_list[1][1],check_list[2][2],check_list[3][3],check_list[4][4]]
    check_diag_2 = [check_list[4][0],check_list[3][1],check_list[2][2],check_list[1][3],check_list[0][4]]
    if (all(check_diag_1) == True) or (all(check_diag_2) == True):
        check_bingo = True
    if check_bingo == True:
        print("ビンゴ！")
    
