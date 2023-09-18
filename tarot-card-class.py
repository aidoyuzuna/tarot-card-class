from enum import Enum


class MajorArcana(Enum):
    FOOL = "愚者"
    MAGICIAN = "魔術師"
    HIGH_PRIESTESS = "女教皇"
    EMPRESS = "女帝"
    EMPEROR = "皇帝"
    HIEROOHANT = "法王"
    LOVERS = "恋人"
    CHARIOT = "戦車"
    STRENGTH = "力"
    HERMIT = "隠者"
    WHEEL_OF_FORTUNE = "運命の輪"
    JUSTICE = "正義"
    HANGED_MAN = "吊るされた男"
    DEATH = "死神"
    TEMPERANCE = "節制"
    DEVIL = "悪魔"
    TOWER = "塔"
    STAR = "星"
    MOON = "月"
    SUN = "太陽"
    JUDGEMENT = "審判"
    WORLD = "世界"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Suit.{self.name}"


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
        return f"Number.{self.name}"


class Element(Enum):
    FIRE = "火"
    EARTH = "土"
    AIR = "風"
    WATER = "水"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Element.{self.name}"


class MajorCard:
    def __init__(self, major_arcana, element):
        if not (isinstance(major_arcana, MajorArcana)):
            raise ValueError
        self.major_arcana = major_arcana
        self.element = element

    def __str__(self):
        return str(self.major_arcana) + str(self.element)

    def __repr__(self):
        return self.__str__()


class MinorCard:
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


major_element = [
    "風",
    "風",
    "水",
    "土",
    "火",
    "土",
    "風",
    "水",
    "火",
    "土",
    "火",
    "風",
    "水",
    "水",
    "火",
    "土",
    "土",
    "風",
    "水",
    "火",
    "火",
    "土",
]

arcana = []
count = 0
for major_arcana in MajorArcana:
    element_item = major_element[count]
    element = Element(element_item)
    arcana.append(MajorCard(major_arcana, element))
    count += 1

minor_arcana = [
    MinorCard(suit, number, element)
    for suit, element in zip(Suit, Element)
    for number in Number
]

print(arcana)
print(minor_arcana)
