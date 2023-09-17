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

minor_arcana = [(suits, numbers) for suits in range(4) for numbers in range(1, 14)]
print(minor_arcana)
