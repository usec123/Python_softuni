STEPS_GOAL = 10_000

steps_made = 0

while steps_made<STEPS_GOAL:
    cmd = input()
    if cmd != 'Going home': steps_made += int(cmd)
    else:
        steps_made+=int(input())
        break
if steps_made<STEPS_GOAL: print(f'{STEPS_GOAL-steps_made} more steps to reach goal.')
else: print(f'Goal reached! Good job!\n{steps_made-STEPS_GOAL} steps over the goal!')