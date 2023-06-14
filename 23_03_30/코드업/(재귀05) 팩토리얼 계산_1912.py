
n = int(input())
# answer = 1
# def factorial(n):
#     global answer
#     if n != 0:
#         factorial(n-1)
#     elif n == 0:
#         n = 1
#     answer = answer * n
#     return answer

# print(factorial(n))

# ------------------------------

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))