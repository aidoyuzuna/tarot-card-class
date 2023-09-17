class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        suits_str = ["ワンド", "ペンタクル", "ソード", "カップ"][self.suit]
        number_str = [
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
        ][self.number]
        return suits_str + number_str

    def __repr__(self):
        return f"Card({self.suit},{self.number})"


minor_arcana = [Card(suit, number) for suit in range(4) for number in range(1, 14)]
print(minor_arcana)
