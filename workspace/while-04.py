import random

#配列生成
sample_num = 50
array_a = list()
for num in range(sample_num):
    array_a.append(random.randint(0, 99))
#print(array_a)

#データ抽出
count_10_20 = 0
count_20_30 = 0
for data in array_a:
    if 10 <= data < 20:
        count_10_20 += 1
    elif 20 <= data <30:
        count_20_30 += 1

print(f'{sample_num}人中…10代は{count_10_20}人、20代は{count_20_30}人です。')
print(f'10代: {round((count_10_20 / sample_num) * 100,2)}%')
print(f'20代: {round((count_20_30 / sample_num) * 100,2)}%')