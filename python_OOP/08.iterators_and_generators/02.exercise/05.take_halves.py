def solution():
    def integers():
        current = 1
        while True:
            yield current
            current += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        # TODO: Implement
        return [next(seq) for _ in range(n)]

    return take, halves, integers


# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
