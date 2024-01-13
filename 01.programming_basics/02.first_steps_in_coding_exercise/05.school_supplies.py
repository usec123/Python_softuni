pen_price = 5.80
marker_price = 7.20
detergent_price = 1.20

pen_count = int(input())
marker_count = int(input())
detergent_litres = int(input())
discount_percentage = int(input())/100

price = (pen_count * pen_price) + (marker_count * marker_price) + (detergent_litres * detergent_price)
price -= price * discount_percentage

print(price)