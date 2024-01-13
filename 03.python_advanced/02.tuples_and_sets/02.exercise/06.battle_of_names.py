n = int(input())

odd_numbers = set()
even_numbers = set()

for x in range(n):
    name = input()
    name = sum(list(map(lambda x: ord(x),name)))//(x+1)
    if name%2==0:
        even_numbers.add(name)
    else:
        odd_numbers.add(name)

sum_odd = sum(odd_numbers)
sum_even = sum(even_numbers)

if sum_odd == sum_even:
    print(', '.join(list(map(str,odd_numbers.union(even_numbers)))))

elif sum_odd > sum_even:
    print(', '.join(list(map(str,odd_numbers.difference(even_numbers)))))

else:
    print(', '.join(list(map(str,odd_numbers.symmetric_difference(even_numbers)))))