calc = lambda product,qty:{'coffee':1.50,'water':1.00,'coke':1.40,'snacks':2.00}.get(product)*qty
print(f'{calc(input(),int(input())):.2f}')