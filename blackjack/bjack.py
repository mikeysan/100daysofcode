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

player.append(deal_card())
computer.append(deal_card())
print(player)
print(computer)
player.append(deal_card())
computer.append(deal_card())
print(player)
print(computer)
computer_score = computer[0] + computer[1]
print(computer_score)
player_score = player[0] + player[1]
print(player_score)
