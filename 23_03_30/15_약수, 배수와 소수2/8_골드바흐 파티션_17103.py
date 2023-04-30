import sys

check = [True] * 1000001
check[0] = False
check[1] = False


for i in range(2, 1000001):
    if check[i]:
        for j in range(2*i, 1000001, i):
            check[j] = False

n = int(sys.stdin.readline())


for i in range(n):
    count = 0
    num = int(sys.stdin.readline())
    for j in range(2, num//2+1):
        if check[j] and check[num-j]:
            count += 1
    print(count)


# ==========================================


# def prime_list(n):
#     sieve = [True] * n
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:         
#             for j in range(2*i, n, i):
#                 sieve[j] = False

#     return [i for i in range(2, n) if sieve[i] == True]