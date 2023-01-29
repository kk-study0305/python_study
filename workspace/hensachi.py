import random
import statistics
import math

# データ生成
data_number = 100
score = []
for i in range(data_number):
    score.append(random.randint(0,100))
print(score)

dev_stat = statistics.pstdev(score)
print(f'ライブラリで求めた偏差値: {dev_stat}')

# 分散を求める
sum_score = 0
ave_score = 0
temp_pva = 0
pvariance = 0

for i in range(data_number):
    sum_score = sum_score + score[i]

ave_score = sum_score / data_number

for i in range(data_number):
    temp_pva = temp_pva + (score[i] - ave_score) * (score[i] - ave_score)

pvariance = temp_pva / data_number
dev_score = math.sqrt(pvariance)
print(f'平均値: {ave_score}')
print(f'偏差値: {dev_score}')
