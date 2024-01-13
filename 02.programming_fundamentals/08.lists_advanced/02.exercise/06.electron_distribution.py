electrons = int(input())
shells = []
while electrons != 0:
	max_electrons = 2*((len(shells)+1)**2)
	if electrons >= max_electrons:
		electrons-=max_electrons
		shells.append(max_electrons)
	else:
		shells.append(electrons)
		electrons = 0
print(shells)