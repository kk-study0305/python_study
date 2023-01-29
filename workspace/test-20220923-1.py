from re import A


array_a = [80, 20, 35]
array_b = [80, 20, 35]
array_c = array_b

print('配列AのID')
print((array_a))
print('配列BのID')
print((array_b))
print('配列CのID')
print((array_c))
print('----------------------')

array_c[2] = 0
print('配列AのID')
print((array_a))
print('配列BのID')
print((array_b))
print('配列CのID')
print((array_c))
    

    