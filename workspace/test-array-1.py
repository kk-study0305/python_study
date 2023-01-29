import re


your_result = []
your_result.append(int(input('国語の点数')))
your_result.append(int(input('英語の点数')))
your_result.append(int(input('社会の点数')))
your_result.append(int(input('数学の点数')))
your_result.append(int(input('理科の点数')))

your_result_sum = sum(your_result)
your_result_ave = your_result_sum / len(your_result)

print(f'合計点は{your_result_sum}、平均点は{your_result_ave}です。')