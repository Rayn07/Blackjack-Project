#Import and Initialization
import random
token = 5
n = 0
round = 1
INIT_DEALT_VALUES = []
CARD_NAME = [
    "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "jack", "king", "queen", "ace"
]
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

#Start
def start_game(round):
    print (f"ROUND {round}:")
    start = input("Press 'ENTER' to start")
    while start != "":
        start = input("Press 'ENTER' to start")

#Pick random cards
def pick(card_value):
    card = CARD_NAME_COPY[random.randint(0, len(CARD_NAME_COPY)-1)]
    CARD_COUNT.update({card: CARD_COUNT[card] - 1})
    if CARD_COUNT[card] == 0:
        CARD_NAME_COPY.remove(card)
    return card_value[card]

#Card count returns back to 4
def card_refresh():
    for card in CARD_NAME:
        CARD_COUNT.update({card: 4})

#Initial Card Distribution
def initial_card_deal(n):
    global user_hand, dealer_hand
    for _ in range (2):
        init_dealt = pick(CARD_VALUE_USER) + pick(CARD_VALUE_USER)
        if init_dealt == 22:
            init_dealt = 12
        INIT_DEALT_VALUES.append(init_dealt)
    dealer_hand = INIT_DEALT_VALUES[n + 0]
    user_hand = INIT_DEALT_VALUES[n + 1]
    print("Dealer's Hand:", dealer_hand, "\nYour Hand:", user_hand)

#Invalid command
def invalid():
    global command
    while command != "h" and command != "s":
        command = input("Enter a valid command: ")

#Logic for the bot to decide whether to hit or stand
def bot_logic():
    global dealer_hand
    diff = 21 - dealer_hand
    while diff > 0:
        diff = 21 - dealer_hand
        if dealer_hand > 10:
                    CARD_VALUE_DEALER.update({"ace": 1})
        if diff >=10:
            dealer_hand = hit(dealer_hand, CARD_VALUE_DEALER)
        else:
            if chance(diff) == True:
                dealer_hand = hit(dealer_hand, CARD_VALUE_DEALER)
            else:
                break
    #if dealer_hand <= 21:
        #print("Dealer stands")

#Hit or Stand
def HitOrStand():
    global command
    global user_hand
    while command.casefold() == "h" or command.casefold() == "s":
        match command:
            case "h":
                if user_hand > 10:
                    CARD_VALUE_USER.update({"ace": 1})
                user_hand = hit(user_hand, CARD_VALUE_USER)
                print("Your Hand:", user_hand)
                if user_hand > 21:
                    print("Oh No! You went bust")
                    stand(user_hand, dealer_hand)
                    break
                command = input("Hit(h) or Stand(s): ")
                invalid()
            case "s":
                stand(user_hand, dealer_hand)
                break

#Chance
def chance(diff):
    psf = 9 - diff #psf = percent subtraction factor
    if random.randint(1,100) <= (70 - (8*psf)):
            return True

#Commands
def hit(hand, card_value):
    hand = hand + pick(card_value)
    return hand

def stand(user_hand, dealer_hand):
    global token
    print("Dealer's Final Hand:", dealer_hand)
    print("Your Final Hand:", user_hand)
    if user_hand > 21 and dealer_hand > 21:
        print("Round draw")
    elif user_hand > 21 and dealer_hand <= 21:
        print("Dealer wins this round")
        token = token//2
    elif dealer_hand > 21 and user_hand <= 21:
        print("You win this round!")
        token = token*2
    elif user_hand > dealer_hand:
        print("You win this round!")
        token = token*2
    elif user_hand == dealer_hand:
        print("Round draw")
    else:
        print("Dealer wins this round")
        token = token//2
    print("Token count:", token)   

#Command to be executed at the end of each round
def round_end():
    global n, round
    if token == 0:
        print ("You lost all your tokens and hence the game")
        exit()
    elif token > 50:
        print("You've earned 50 tokens!\nYou WIN!!")
        exit()
    card_refresh()
    n += 2
    round += 1

#Main Block
print ("Welcome to Ray's BlackJack!\n> In order to win, you must earn 50 tokens.\n> If you lose all of your tokens, the game will end.\n> GOOD LUCK!")
while token < 50:
    CARD_NAME_COPY = CARD_NAME.copy()
    start_game(round)
    initial_card_deal(n)
    bot_logic()
    command = input("Hit(h) or Stand(s): ")
    invalid()
    HitOrStand()
    round_end()