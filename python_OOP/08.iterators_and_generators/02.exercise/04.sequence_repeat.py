class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration()
        self.number -= 1
        if not self.current_sequence:
            self.current_sequence = self.sequence
        output = self.current_sequence[0]
        self.current_sequence = self.current_sequence[1::] if len(self.current_sequence) > 1 else None
        return output


# result = sequence_repeat('abc', 5)
#
# for item in result:
#     print(item, end='')


result = sequence_repeat('I Love Python', 3)

for item in result:
    print(item, end='')
