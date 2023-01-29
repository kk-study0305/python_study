from itertools import count
from logging import logProcesses


loop_count = 0

#条件式がTrueの間動作し続ける。
while loop_count < 5:
    print(f'これは{loop_count + 1}回目のループです。')
    if (loop_count + 1) % 2 == 0:
        print('偶数ループ')
    loop_count += 1
print('終了')