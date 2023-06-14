import sys
sys.setrecursionlimit (10**8)

# n = int(input())

# answer = 0

# def plus(n):
#     global answer
#     if n != 0:
#         plus(n-1)
#     answer += n
#     return answer
# print(plus(n))


# -----------------



n = 100

def plus(n):
    if n == 1:
        return 1
    return n + plus(n-1)

print(plus(n))