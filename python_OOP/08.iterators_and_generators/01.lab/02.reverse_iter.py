class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index < 0:
            raise StopIteration()
        index = self.start_index
        self.start_index -= 1
        return self.iterable[index]


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)
