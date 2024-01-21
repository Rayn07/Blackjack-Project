from Pick import pick
import Variables as v

def hit(hand, card_value):
    picked = pick(card_value)
    card = picked[1]
    hand = hand + picked[0]
    return hand, card

def stand(user, dealer):
    tok = int(v.token.get())
    print("Dealer's Final Hand:", dealer)
    print("Your Final Hand:", user)
    if user > 21 and dealer > 21:
        print("Round draw")
        v.round_result.set(value="Round Draw")
    elif user > 21 and dealer <= 21:
        print("Dealer wins this round")
        v.token.set(tok // 2)
        v.round_result.set(value="Round Lost")
    elif dealer > 21 and user <= 21:
        print("You win this round!")
        v.token.set(tok * 2)
        v.round_result.set(value="Round Won")
    elif user > dealer:
        print("You win this round!")
        v.token.set(tok * 2)
        v.round_result.set(value="Round Won")
    elif user == dealer:
        print("Round draw")
        v.round_result.set(value="Round Draw")
    else:
        print("Dealer wins this round")
        v.token.set(tok // 2)
        v.round_result.set(value="Round Lost")