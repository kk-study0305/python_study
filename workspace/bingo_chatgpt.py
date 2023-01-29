import random

# 5x5のカードを作成
card = [[0 for x in range(5)] for y in range(5)]

# カードに1から75の数字を割り当て
n = 0
for i in range(5):
    for j in range(5):
        if i == 0:
            card[i][j] = n + 1
        elif i == 1:
            card[i][j] = n + 16
        elif i == 2:
            card[i][j] = n + 31
        elif i == 3:
            card[i][j] = n + 46
        elif i == 4:
            card[i][j] = n + 61
        n += 1
        if n % 15 == 0:
            n = 0
#中央にFREEを入れる
card[2][2] = "FREE"

# 番号を抽選
drawn_numbers = []
while len(drawn_numbers) < 25:
    drawn_number = random.randint(1, 75)
    if drawn_number not in drawn_numbers:
        drawn_numbers.append(drawn_number)

# 抽選番号がカード上にあるか確認
for drawn_number in drawn_numbers:
    for i in range(5):
        for j in range(5):
            if card[i][j] == drawn_number:
                card[i][j] = "X"

# ビンゴが成立しているか確認
bingo = False
for i in range(5):
    if card[i].count("X") == 5:
        bingo = True
        break
    if all(card[x][i] == "X" for x in range(5)):
        bingo = True
        break
    if all(card[x][x] == "X" for x in range(5)):
        bingo = True
        break
    if all(card[x][4-x] == "X" for x in range(5)):
        bingo = True
        break
if bingo:
    print("BINGO!")
else:
    print("No BINGO.")
