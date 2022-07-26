import random
from art import logo


def deal_card():
    """
    Generate a random number/card from the list.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


player = []
computer = []


play = True


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == "y":
    print(logo)
    player.append(deal_card())
    player.append(deal_card())
    computer.append(deal_card())
    computer.append(deal_card())
    score = sum(player)
    print(f"Your cards: {player}, current score: {score}")
    print(f"Computer's first card: {computer[0]}")
else:
    print("Maybe you will play later. Bye!")

while play:
    if score > 21:
        computer_score = sum(computer)
        print(f"Your final hand: {player}, final score: {score}")
        print(f"Computer's final hand: {computer}, final score: {computer_score}")
        play = False
    else:
        deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal == "n":
            print(f"Your cards: {player}, final score: {score}")
            print(computer)
            computer_score = sum(computer)
            player_score = sum(player)
            print(f"Your final hand: {player}, final score: {player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            if player_score < computer_score:
                print("Dealer wins!")
            elif player_score == computer_score:
                print("Draw!")
            elif player_score == 21 and computer_score ==21:
                print("Dealer wins!")
            elif player_score > 21:
                print("Dealer wins!")
            else:
                print("Player wins!")
            play = False
        else:
            if score > 21:
                print("Dealer wins!")
            else:
                player.append(deal_card())
                score = sum(player)
                print(f"Your cards: {player}, current score: {score}")
