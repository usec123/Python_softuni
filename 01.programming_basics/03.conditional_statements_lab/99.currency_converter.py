from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input('Enter currency amount: '))

# USD, EUR, BGN
from_currency = input('From currency: ')
to_currency = input('To currency: ')

result = c.convert(from_currency, to_currency, amount)

print(f'{result:.2f}')