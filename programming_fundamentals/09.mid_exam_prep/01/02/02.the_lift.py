people_waiting = int(input())
state = list(map(int,input().split()))
MAX_PEOPLE_ON_WAGON = 4

for x in range(len(state)):
    people_getting_on = MAX_PEOPLE_ON_WAGON-state[x]
    if people_getting_on<=people_waiting:
        state[x] += people_getting_on
        people_waiting -= people_getting_on
    else:
        state[x]+=people_waiting
        people_waiting=0

if people_waiting == 0:
    if sum(state) != len(state)*MAX_PEOPLE_ON_WAGON:
        print('The lift has empty spots!')
    print(' '.join([str(item) for item in state]))
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join([str(item) for item in state])}")