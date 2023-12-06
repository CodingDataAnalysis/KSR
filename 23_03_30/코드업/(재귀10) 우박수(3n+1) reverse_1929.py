
n = int(input())

def three(n):
    if n == 1:
        return print(n)

    else:
        if n % 2 != 0:
            three(3 * n + 1)
            print(n)
        elif n % 2 == 0:
            three(n // 2)
            print(n)

three(n)