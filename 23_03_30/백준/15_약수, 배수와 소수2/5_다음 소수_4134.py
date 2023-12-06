def prime(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[i] = False
    return [i for i in range(2, n) if sieve[i] == False]

print(prime(5))


