class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = 1
        for x in args:
            res *= x
        return res

    @staticmethod
    def divide(*args):
        num = args[0]
        for x in args[1::]:
            num /= x
        return num

    @staticmethod
    def subtract(*args):
        num = args[0]
        for x in args[1::]:
            num -= x
        return num
