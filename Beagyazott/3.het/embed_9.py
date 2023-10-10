from time import time

def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:a
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

# Input a number from the user
n = int(input('N: '))

# Start the timer
start = time()

# Perform prime factorization
result = prime_factors(n)

# Stop the timer
end = time()

print("Prime factors of {}: {}".format(n, result))
print("Elapsed time: {:.6f} seconds".format(end - start))
