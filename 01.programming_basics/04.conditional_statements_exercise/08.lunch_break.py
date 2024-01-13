from math import ceil

film = input()
episode_length = int(input())
break_length = int(input())

lunch_time = 1/8*break_length
break_time = 1/4*break_length
time = break_length - lunch_time - break_time

if time>=episode_length: print(f'You have enough time to watch {film} '+
    f'and left with {ceil(time-episode_length)} minutes free time.')
else: print(f"You don't have enough time to watch {film}, "+
    f"you need {ceil(episode_length-time)} more minutes.")