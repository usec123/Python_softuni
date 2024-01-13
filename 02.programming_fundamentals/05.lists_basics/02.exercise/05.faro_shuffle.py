cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    cards_1 = cards[:int(len(cards)/2)]
    cards_2 = cards[int(len(cards)/2):]
    cards = []
    while len(cards_1) > 0 and len(cards_2) > 0:
        cards.append(cards_1.pop(0))
        cards.append(cards_2.pop(0))
print(cards)