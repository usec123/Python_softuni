population = list(map(int,input().split(', ')))
min_wealth = int(input())
possible = True


while min(population) < min_wealth:
    max_index = population.index(max(population))
    min_index = population.index(min(population))
    
    needed_money = min_wealth - population[min_index]
    if population[max_index] - needed_money < min_wealth:
        possible = False
        break
    else:
        population[min_index] += needed_money
        population[max_index] -= needed_money

if possible: print(population)
else: print('No equal distribution possible')