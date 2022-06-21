deck_of_cards = input().split()
count_of_shuffles = int(input())

for current_shuffle in range(count_of_shuffles):
    ready_deck = []
    left_half = deck_of_cards[:len(deck_of_cards) // 2]
    right_half = deck_of_cards[len(deck_of_cards) // 2:]
    for curernt_card in range(len(left_half)):
        ready_deck.append(left_half[curernt_card])
        ready_deck.append(right_half[curernt_card])
    deck_of_cards = ready_deck
print(deck_of_cards)