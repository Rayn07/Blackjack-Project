from copy import deepcopy

INIT_DEALT_VALUES = []
CARDS = {
    "spades": {
        "ace": "🂡","two": "🂢", "three": "🂣", "four": "🂤", "five": "🂥", "six": "🂦", "seven": "🂧",
        "eight": "🂨", "nine": "🂩", "ten": "🂪", 'jack': "🂫", "queen": "🂭", "king": "🂮"
    },

    "hearts": {
        "ace": "🂱","two": "🂲", "three": "🂳", "four": "🂴", "five": "🂵", "six": "🂶", "seven": "🂷",
        "eight": "🂸", "nine": "🂹", "ten": "🂺", 'jack': "🂻", "queen": "🂽", "king": "🂾"
    },

    "diamonds": {
        "ace": "🃁","two": "🃂", "three": "🃃", "four": "🃄", "five": "🃅", "six": "🃆", "seven": "🃇",
        "eight": "🃈", "nine": "🃉", "ten": "🃊", 'jack': "🃋", "queen": "🃍", "king": "🃎"
    },

    "clubs": {
        "ace": "🃑","two": "🃒", "three": "🃓", "four": "🃔", "five": "🃕", "six": "🃖", "seven": "🃗",
        "eight": "🃘", "nine": "🃙", "ten": "🃚", 'jack': "🃛", "queen": "🃝", "king": "🃞"
    }
}
CARD_NAME = [
    "ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "jack", "queen", "king"
]
CARD_SUITS = ["spades", "hearts", "diamonds", "clubs"]
CARD_COUNT = {
    "two": 4, "three": 4, "four": 4, "five": 4, "six": 4, "seven": 4, "eight": 4, "nine": 4, "ten": 4,
    "jack": 4, "king": 4, "queen": 4, "ace": 4
}
CARD_VALUE_USER = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "jack": 10, "king": 10, "queen": 10, "ace": 11
}
CARD_VALUE_DEALER = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "jack": 10, "king": 10, "queen": 10, "ace": 11
}
CARDS_COPY = deepcopy(CARDS)
CARD_NAME_COPY = CARD_NAME.copy()