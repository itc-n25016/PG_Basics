answer = input("好きな食べ物は何ですか？: ")

with open("food.txt", "w", encoding="utf-8") as file:
    file.write("ユーザーの好きな食べ物: " + answer + "\n")

print("回答をファイルに保存しました。")

