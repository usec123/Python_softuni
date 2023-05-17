cmd = input()
sum = 0

while cmd != 'NoMoreMoney':
    if float(cmd)>0:
        print(f'Increase: {float(cmd):.2f}')
        sum += float(cmd)
        cmd = input()
    else:
        print('Invalid operation!')
        break

print(f'Total: {sum:.2f}')