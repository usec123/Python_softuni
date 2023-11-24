from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if type(value) is not float:
            return 'value is not a float'
        return cls(floor(value))

    @classmethod
    def from_roman(cls, value: str):
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        for i in range(len(value)):
            if value[i] in mapper:
                if i + 1 < len(value) and mapper[value[i]] < mapper[value[i + 1]]:
                    res -= mapper[value[i]]
                else:
                    res += mapper[value[i]]
            else:
                break

        return cls(res)
    @classmethod
    def from_string(cls, value: str):
        try:
            if not isinstance(value, str):
                raise ValueError
            return cls(int(value))
        except ValueError:
            return 'wrong type'
