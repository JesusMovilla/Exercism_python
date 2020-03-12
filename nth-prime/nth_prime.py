import math


def prime(number):
    primes = []
    primes.append(2)
    if number < 1:
        raise ValueError(ValueError)
    n = 3
    while len(primes) < number:
        prime = True
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i) == 0:
                prime = False
                break
        if prime:
            primes.append(n)
        n += 2
    return primes[number-1]
