def possible_permutations(list):
    if len(list) <= 1:
        yield list
    else:
        for i in range(len(list)):
            for permutation in possible_permutations(list[:i:] + list[i+1::]):
                yield [list[i]] + permutation


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
