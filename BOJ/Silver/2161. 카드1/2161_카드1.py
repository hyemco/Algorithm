N = int(input())

cards = [i for i in range(1, N + 1)]

discard_card = []

while len(cards) != 1:
    discard_card.append(cards.pop(0))
    cards.append(cards.pop(0))

for card in discard_card:
    print(card, end = ' ')
print(cards[0])