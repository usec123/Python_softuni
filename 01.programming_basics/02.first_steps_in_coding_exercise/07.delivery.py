CHICKEN_PRICE = 10.35
FISH_PRICE = 12.4
VEGETARIAN_PRICE = 8.15

chicken_num = int(input())
fish_num = int(input())
vegetarian_num = int(input())

sum = CHICKEN_PRICE*chicken_num
sum += FISH_PRICE*fish_num
sum += VEGETARIAN_PRICE*vegetarian_num
sum *= 1.2
sum += 2.5

print(sum)