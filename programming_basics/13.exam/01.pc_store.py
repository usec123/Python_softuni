USD_TO_BGN = 1.57

#prices in BGN
processor_price = float(input())*USD_TO_BGN  #discount
video_card_price = float(input())*USD_TO_BGN #discount
ram_price = float(input())*USD_TO_BGN
ram_qty = int(input())
discount = float(input())

ram_price *= ram_qty

processor_price -= processor_price*discount
video_card_price-=video_card_price*discount

total = processor_price+video_card_price+ram_price

print(f'Money needed - {total:.2f} leva.')