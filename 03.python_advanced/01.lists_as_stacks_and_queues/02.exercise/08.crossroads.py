from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
line = input()
cars = deque()
cars_counter = 0
crashed = False

def green_light():
    global cars_counter,crashed
    
    if cars:
        current_car = cars.popleft()
        left_seconds = green_light_duration - len(current_car)
        
        while left_seconds > 0:
            cars_counter += 1
            
            if not cars:
                break
            
            current_car = cars.popleft()
            left_seconds -= len(current_car)
            
        if left_seconds == 0:
            cars_counter += 1
            
        if free_window_duration >= abs(left_seconds):
            if left_seconds < 0:
                cars_counter += 1
                
        else:
            index = free_window_duration + left_seconds
            print(f"A crash happened!\n{current_car} was hit at {current_car[index]}.")
            crashed = True

while line != "END":
    if line == "green":
        green_light()
        
        if crashed:
            break
        
    else:
        cars.append(line)
        
    line = input()

if not crashed:
    print(f"Everyone is safe.\n{cars_counter} total cars passed the crossroads.")