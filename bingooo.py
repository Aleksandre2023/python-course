# Guess the Bingo number

import random

def generate_bingo_card():
    # Initialize an empty 5x5 Bingo card as a list of lists
    card = [['B', 'I', 'N', 'G', 'O']]
    for _ in range(2):
        row = random.sample(range(1, 99), 5)  # Get 5 unique random numbers from 1 to 99
        card.append(row)
    return card

def display_bingo_card(card):
    for row in card:
        print(' '.join(str(num).rjust(2) if isinstance(num, int) else num.center(2) for num in row))

if __name__ == "__main__":
    bingo_card = generate_bingo_card()
    display_bingo_card(bingo_card)
