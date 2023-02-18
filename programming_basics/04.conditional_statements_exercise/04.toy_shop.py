PUZZLE = 2.6
DOLL = 3
BEAR = 4.10
MINION = 8.2
TRUCK = 2

exc_price = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

total = puzzle*PUZZLE+doll*DOLL+bear*BEAR+minion*MINION+truck*TRUCK
cnt = puzzle+doll+bear+minion+truck

if cnt >= 50: total*=0.75
total *= 0.9

if total>=exc_price:print(f'Yes! {(total - exc_price):.2f} lv left.')
else: print(f'Not enough money! {(exc_price - total):.2f} lv needed.')