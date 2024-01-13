numbers = sorted(list(map(int,input().split())))

avg = sum(numbers)/len(numbers)

chosen_numbers = [str(num) for num in numbers if num>avg][:-6:-1]

print(' '.join(chosen_numbers) if len(chosen_numbers)>0 else 'No')