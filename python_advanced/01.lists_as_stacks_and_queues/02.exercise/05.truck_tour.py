def check_pump(index:int)->bool:
    fuel = 0
    for x in range(number_of_pumps):
        fuel += petrol_amount[(index+x)%number_of_pumps]
        fuel -= distance[(index+x)%number_of_pumps]
        if fuel<0: return False
    return True

number_of_pumps = int(input())
petrol_amount = []
distance = []
for _ in range(number_of_pumps):
    text = list(map(int,input().split()))
    petrol_amount.append(text[0])
    distance.append(text[1])

for x in range(number_of_pumps):
    if check_pump(x):
        print(x)
        break