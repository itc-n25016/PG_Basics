import csv

data = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]

file_name = "movies.csv"

with open(file_name, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

print(f"{file_name} に映画データを書き出しました。")

