file_path = "Challenge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("Challenge.txt の内容:")
    print(content)

