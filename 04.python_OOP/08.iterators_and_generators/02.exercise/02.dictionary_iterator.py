class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.start_index = 0
        self.end_index = len(dictionary) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index > self.end_index:
            raise StopIteration()
        index = self.start_index
        self.start_index += 1
        return (list(self.dictionary.keys())[index],
                self.dictionary[list(self.dictionary.keys())[index]])


# result = dictionary_iter({1: "1", 2: "2"})
#
# for x in result:
#     print(x)

result = dictionary_iter({"name": "Peter", "age": 24})

for x in result:
    print(x)
