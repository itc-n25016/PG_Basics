import csv

# 日本語映画データ
data = [
    ["トップガン", "リスキー・ビジネス", "マイノリティ・リポート"],
    ["タイタニック", "レヴェナント", "インセプション"],
    ["トレーニング・デイ", "マイ・ボディガード", "フライト"]
]

# 書き込み先のファイル名
file_name = "movies_jp.csv"

# CSVファイルに書き出し
with open(file_name, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

print(f"{file_name} に日本語の映画データを書き出しました。")

