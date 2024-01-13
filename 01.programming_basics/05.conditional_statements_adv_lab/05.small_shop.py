SOFIA_PRICES = [0.5,0.8,1.2,1.45,1.6]
PLOVDIV_PRICES = [0.4,0.7,1.15,1.3,1.5]
VARNA_PRICES = [0.45,0.7,1.1,1.35,1.55]
PRODUCTS = ['coffee', 'water', 'beer', 'sweets', 'peanuts']

product = input()
city = input()
qty = float(input())

if city == 'Sofia':
    price = qty*SOFIA_PRICES[PRODUCTS.index(product)]
if city == 'Plovdiv':
    price = qty*PLOVDIV_PRICES[PRODUCTS.index(product)]
if city == 'Varna':
    price = qty*VARNA_PRICES[PRODUCTS.index(product)]

print(round(price,2))