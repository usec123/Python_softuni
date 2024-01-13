movie_type = input()
rows, cols = int(input()), int(input())

seats = rows * cols

if (movie_type == 'Premiere'): price  = 12.00
elif (movie_type  == 'Normal'): price = 7.50
else: price = 5.00

total = seats * price

print(f'{total:.2f} leva')