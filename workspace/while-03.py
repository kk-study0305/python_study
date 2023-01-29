import random
count = 0
ele_num = 6
array_a = list()
#配列A
count_a = 0
while count_a <= ele_num:
    array_a.append(random.randint(0, 9))
    count_a += 1
#配列B

for num in array_a:
    print(f'{num}')