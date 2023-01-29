import random
eat_number = 0
bite_number = 0

challenge_number = 0

# 正解作成
correct_list = []
while len(correct_list) < 3:
    n = random.randint(0, 9)
    if not n in correct_list:
        correct_list.append(n)

while eat_number != 3:
    challenge_number += 1
    # ユーザーの入力した3桁の数字を3要素の数値配列に変換
    print(f'{challenge_number}回目の挑戦です。')
    print("答えを入力してください>>>")
    your_anser = str(input())
    your_list_str = list(your_anser)
    your_list = list(map(int, your_list_str))

    # 配列の比較
    # 同じ数値かつインデックスが等しければEAT、同じ数値かつインデックスが異なればBITEとする
    eat_number = 0
    bite_number = 0
    for i in range(3):
        if correct_list[i] == your_list[i]:
            eat_number += 1
        elif your_list[i] in correct_list:
            bite_number += 1
    print(f'{eat_number} EAT. {bite_number} BITE.')
    

print(f'おめでとうございます。{challenge_number}回目でクリアです。')
    

