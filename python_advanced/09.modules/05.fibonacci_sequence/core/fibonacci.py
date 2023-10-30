from math import inf

def fib_sequence(count = inf, number = inf, num1=0, num2=1):
    sequence = []
    sequence.append(0)
    sequence.append(1)
    
    def fib_sequence_internal(count, number, num1, num2):
        if count == 0:
            return ' '.join(list(map(str,sequence)))
        if num2 >= number:
            if num2==number:
                return f'The number - {number} is at index {len([item for item in sequence if item<number])}'
            else:
                return f'The number {number} is not in the sequence'

        num = num1+num2
        sequence.append(num)
        return fib_sequence_internal(count-1, number, num2, num)
    
    return fib_sequence_internal(count,number,num1,num2)