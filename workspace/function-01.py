#関数定義
def hello():
    print('hello')
#関数呼び出し
hello()

#引数付き関数
def hello_arg(text_a, text_b, text_c):
    print(f'入力したのは”{text_a}”,”{text_b}”,”{text_c}”ですね。')
#関数呼び出し
hello_arg(input('何か入力してください>>>'),input('何か入力してください>>>'),input('何か入力してください>>>'))