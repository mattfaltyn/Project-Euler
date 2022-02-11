import numpy as np
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

x = np.arange(1, 10**6)

foo = np.vectorize(is_prime)
pbools = foo(x)
primes = np.extract(pbools, x)
primes[10001]