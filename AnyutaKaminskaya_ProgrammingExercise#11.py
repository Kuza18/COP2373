# This program deals a Poker hand of five cards, lets the user replace cards,
# then prints the new hand.
# The random package gives us shuffle(), which mixes up a list.
import random


# Deck class
class Deck():
    # Create the deck and shuffle it
    def __init__(self, n_decks=1):
        # Make all 52 cards as a rank plus a suit symbol
        self.card_list = [num + suit
            for suit in '\u2665\u2666\u2663\u2660'
            for num in 'A23456789TJQK'
            for deck in range(n_decks)]
        # Cards that have been dealt are on the table
        self.cards_in_play_list = []
        # Cards from finished hands
        self.discards_list = []
        # shuffle() rearranges the list
        random.shuffle(self.card_list)

    # Deal one card from the deck and return it.
    def deal(self):
        # If the deck has run out, shuffle the cards and use them as the new deck.
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!')
        # pop() removes last card from the lsit and gives it to us
        new_card = self.card_list.pop()
        # Keep track of the card on the table
        self.cards_in_play_list.append(new_card)
        return new_card

    # Move the cards in play to the discard pile when a hand is over
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

# Print each card with its number in front of it.
def print_hand(hand):
    for i in range(5):
        print(i + 1, ':', hand[i])

# Ask user which cards to replace and checks for input error.
def get_choices():
    digits = ['1', '2', '3', '4', '5']
    words = ['one', 'two', 'three', 'four', 'five']

    while True:
        ans = input("Enter cards to replace (for example: 1, 3, 5): ")
        items = ans.lower().replace(',', ' ').split()
        # Go through the items and turn each valid one into a number.
        ## Invalid ones are skipped.
        choices = []
        for item in items:
            if item in digits:
                choices.append(int(item))
            # 'one' is at index 0, so add 1 to get the number
            elif item in words:
                choices.append(words.index(item) + 1)

        # If nothing was skipped (errors), then the input was valid and is returned to user.
        if len(items) > 0 and len(choices) == len(items):
            return choices

        # If something was skipped, the 2 lists aren't equal, and they are prompted again.
        print("Invalid entry. Use only numbers 1 to 5.")

# Deal a new card into each position the user picked.
# Lists are changed inplace, so the hand in main() is updates and nothing needs to be returned.
def draw_cards(deck, hand, choices):
    for num in choices:
        hand[num - 1] = deck.deal()

# Runs the whole program: deal the hand, do the draw, and print the result.
def main():
    my_deck = Deck()
    hand = []
    for i in range(5):
        hand.append(my_deck.deal())

    print('Your hand:')
    print_hand(hand)

    choices = get_choices()
    draw_cards(my_deck, hand, choices)

    print('Your new hand:')
    print_hand(hand)

main()
