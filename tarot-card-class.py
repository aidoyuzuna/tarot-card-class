from enum import Enum, auto


class Suit(Enum):
    WAND = "ワンド"
    PENTACLE = "ペンタクル"
    SWORD = "ソード"
    CUP = "カップ"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Suit.{self.name}"


class Number(Enum):
    ACE = (1, "A")
    TWO = (2, "2")
    THREE = (3, "3")
    FOUR = (4, "4")
    FIVE = (5, "5")
    SIX = (6, "6")
    SEVEN = (7, "7")
    EIGHT = (8, "8")
    NINE = (9, "9")
    TEN = (10, "10")
    KNIHT = (11, "J")
    PAGE = (12, "P")
    QUEEN = (13, "Q")
    KING = (14, "K")

    def __init__(self, val, string):
        self.val = val
        self.string = string

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"Number.(self.name)"


class Element(Enum):
    FIRE = "火"
    EARTH = "土"
    AIR = "風"
    WATER = "水"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Suit.{self.name}"


class Card:
    def __init__(self, suit, number, element):
        if not (
            isinstance(suit, Suit)
            and isinstance(number, Number)
            and isinstance(element, Element)
        ):
            raise ValueError
        self.suit = suit
        self.number = number
        self.element = element

    def __str__(self):
        return str(self.suit) + str(self.number) + str(self.element)

    def __repr__(self):
        return self.__str__()


minor_arcana = [
    Card(suit, number, element)
    for suit, element in zip(Suit, Element)
    for number in Number
]
print(minor_arcana)
