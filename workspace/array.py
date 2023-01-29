#リストについて
list_example = [1, 2, 3, 4]
#sum…リスト内の数値の合計
print(sum(list_example))

#len…リスト内の要素数を算出
print(len(list_example))

#リストの末尾に要素を追加
list_example.append(5)
print(list_example)

#リストの要素を削除
list_example.remove(5)
print(list_example)

#リストの要素を変更
list_example[1] = 5
print(list_example)

#リストの範囲指定
a = 1
b = 3
print(list_example[a:b])