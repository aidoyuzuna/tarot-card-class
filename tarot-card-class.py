minor_arcana = []
suits = ["ワンド", "ペンタクル", "ソード", "カップ"]
numbers = [
    "エース",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "ナイト",
    "ペイジ",
    "クイーン",
    "キング",
]

for su in suits:
    for num in numbers:
        minor_arcana.append(su + num)

print(minor_arcana)
