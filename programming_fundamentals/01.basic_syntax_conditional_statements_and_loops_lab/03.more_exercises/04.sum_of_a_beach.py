cmd = input().lower()
sand = len(cmd.split('sand'))-1
water = len(cmd.split('water'))-1
fish = len(cmd.split('fish'))-1
sun = len(cmd.split('sun'))-1
print(sand+water+fish+sun)