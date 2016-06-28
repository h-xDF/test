from itertools import *

#x = [i in range(31)]

def IsPrimse(x):
    if x % 2 and x > 2:
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
    elif x != 2:
        return False
    return True

def primes(x):
    for i in range(31):
        if IsPrimse(i):
            yield i

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
