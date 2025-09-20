import random
from art import logo

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    card = random.choice(cards)
    cards.remove(card)  # Remove it from deck so no duplicates
    return card


# Function to calculate the score of a hand
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2: # Check for blackjack (2 cards: Ace + 10)
        return 0  # 0 represents blackjack

    # Adjust for Ace (11 -> 1) if total > 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # remove the Ace
        cards.append(1)  # replace it with 1

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Computer has Blackjack! You lose"
    elif u_score == 0:
        return "You have Blackjack! You win"
    elif u_score > 21:
        return "You went over 21! You lose"
    elif c_score > 21:
        return "Computer went over 21! You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal 2 cards to user
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards:, {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score:, {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()




