def get_primes(integers):
    for x in integers:
        if x > 1 and is_prime(x):
            yield x


def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
