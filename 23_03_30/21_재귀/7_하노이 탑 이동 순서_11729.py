import sys

# k = int(sys.stdin.readline())
k = 3


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)

    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

print(2** k-1)
hanoi(k, 1, 2, 3)


'''
3 / 1, 2, 3


'''