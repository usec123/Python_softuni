class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    # iter points to which item from the class is going to be iterable
    # in this case, we will iterate through the class itself, hence why we return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration()
        temp = self.start
        self.start += 1
        return temp


one_to_ten = custom_range(1, 10)

for num in one_to_ten:
    print(num)
