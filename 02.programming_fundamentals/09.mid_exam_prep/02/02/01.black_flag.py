days = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())

plunder = 0

for x in range(1,days+1):
    plunder+=plunder_per_day
    if x % 3 == 0:
        plunder+=plunder_per_day/2
    if x % 5 == 0:
        plunder*=0.7

if plunder>=expected_plunder: print(f'Ahoy! {plunder:.2f} plunder gained.')
else:print(f'Collected only {((plunder/expected_plunder)*100):.2f}% of the plunder.')