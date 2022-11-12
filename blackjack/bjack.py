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


while play:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player.append(deal_card())
    player.append(deal_card())
    computer.append(deal_card())
    computer.append(deal_card())
    print(player)
    print(computer[0])
    deal = print("Type 'y' to get another card, type 'n' to pass: ")
    if deal == "n":
        print(player)
        print(computer)
        computer_score = computer[0] + computer[1]
        player_score = player[0] + player[1]
        if player_score < computer_score:
            print("Dealer wins!")
        elif player_score == computer_score:
            print("Draw!")
        else:
            print("Player wins!")
        play = False
    else:
        player.append(deal_card())
        print(player)

# player.append(deal_card())
# computer.append(deal_card())
# print(player)
# print(computer)
# computer_score = computer[0] + computer[1]
# print(computer_score)
# player_score = player[0] + player[1]
# print(player_score)
