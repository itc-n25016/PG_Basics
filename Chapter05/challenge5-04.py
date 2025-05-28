me = {
    "height": "170",
    "fav_color": ["white", "black", "light blue"],
    "fav_food": ["ラーメン", "カレー"]
}

print(me)

answer = input("Type height, fav_color or fav_food")
if answer in me:
    result = me[answer]
    print(result)
