isError = int(input('0か1を入力してください>>'))
n = int(input('好きな整数を入力してください>>'))
print('-----------------------------------')
if not(isError == 1 or isError == 0):
    print('何を入力してるんですか？') 
elif isError == False and n < 100:
    print('条件に合致しています')
elif isError == False:
    print('整数が100以上です')
elif n < 100:
    print('0を入力していません')
else:
    print('どちらにも合致していません')