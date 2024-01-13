class vowels:
    def __init__(self, text: str):
        self.text = [char for char in text if char.lower() in 'aeiouy']
        self.start_index = 0
        self.end_index = len(self.text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index == self.end_index:
            self.start_index = 0
            raise StopIteration()
        character = self.text[self.start_index]
        self.start_index += 1
        return character


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
