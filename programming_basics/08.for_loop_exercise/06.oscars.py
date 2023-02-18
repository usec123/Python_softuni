actor_name = input()
points = float(input())
voters = int(input())

for _ in range(0,voters):
    voter_name = input()
    voted_points = float(input())
    if points>1250.5: continue
    points += len(voter_name) * voted_points / 2
if (points > 1250.5): print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
else: print(f'Sorry, {actor_name} you need {1250.5-points:.1f} more!')