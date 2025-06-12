numbers = [10,20,30,40,50]

while True:
    answer = input("数字を入力してください(qを入力すると終了)")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか,qで終了します")
    if answer in numbers:
        print("正解")
    else:
        print("不正解")
