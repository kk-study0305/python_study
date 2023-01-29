import math
number = float(input('数値を入力してください'))
if float(number) == float(math.floor(number)):
    number = int(number)
    if number % 2 == 0:
        print(f'{number}は偶数')
    else: 
        print(f'{number}は奇数')
else:
    print(f'{number}は整数ではありません')
