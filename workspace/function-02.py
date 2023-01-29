import random
#関数定義
#配列生成
def gen_array(element_num):
    array = list()
    for num in range(element_num):
        array.append(random.randint(0, 99))
    return array
#配列分析
def ana_array(num_array):
    count_10_20 = 0
    count_20_30 = 0
    for data in num_array:
        if 10 <= data < 20:
            count_10_20 += 1
        elif 20 <= data <30:
            count_20_30 += 1
    print(num_array)
    print(f'{len(num_array)}人中…10代は{count_10_20}人、20代は{count_20_30}人です。')
    print(f'10代: {round((count_10_20 / len(num_array)) * 100,2)}%')
    print(f'20代: {round((count_20_30 / len(num_array)) * 100,2)}%')
    
#関数呼び出し
array_a = gen_array(int(input('データ数を入力してください>>>')))
ana_array(array_a)
array_b = gen_array(int(input('データ数を入力してください>>>')))
ana_array(array_b)