#Lazy Evaluation with Generators
def prime_numbers(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, limit + 1):
        if sieve[num]:
            yield num
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

def first_n_primes(n):
    primes = prime_numbers(10**6)
    return [next(primes) for _ in range(n)]

print(first_n_primes(10))
