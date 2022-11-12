import random


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
        else:
            print("Player wins!")
        play = False
    else:
        player.append(deal_card())        
        score = sum(player)
        print(f"Your cards: {player}, current score: {score}")


