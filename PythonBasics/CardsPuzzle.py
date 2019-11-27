"""
Problem statement:
    - Let's assume that we have a deck of cards.
    - Shuffle the cards
    - Pick one Random card
    - Again pick another random card. Make sure that the first picked should not come again as it is already picked.
"""

from random import shuffle


def create_deck_of_cards():
    # 4 Types of Cards - HEART, DIAMOND, SPADE & FLOWER
    cards = {
        1: "HA", 2: "H2", 3: "H3", 4: "H4", 5: "H5", 6: "H6", 7: "H7", 8: "H8", 9: "H9", 10: "H10", 11: "HJ", 12: "HQ",
        13: "HK",
        14: "DA", 15: "D2", 16: "D3", 17: "D4", 18: "D5", 19: "D6", 20: "D7", 21: "D8", 22: "D9", 23: "D10", 24: "DJ",
        25: "DQ", 26: "DK",
        27: "FA", 28: "F2", 29: "F3", 30: "F4", 31: "F5", 32: "F6", 33: "F7", 34: "F8", 35: "F9", 36: "F10", 37: "FJ",
        38: "FQ", 39: "FK",
        40: "SA", 41: "S2", 42: "S3", 43: "S4", 44: "S5", 45: "S6", 46: "S7", 47: "S8", 48: "S9", 49: "S10", 50: "SJ",
        51: "SQ", 52: "SK"
    }

    shuffled_cards = list(range(1, 53))
    shuffle(shuffled_cards)
    print(cards.pop(shuffled_cards.pop()))
    print(cards.pop(shuffled_cards.pop()))


def main():
    create_deck_of_cards()


if __name__ == '__main__':
    main()
