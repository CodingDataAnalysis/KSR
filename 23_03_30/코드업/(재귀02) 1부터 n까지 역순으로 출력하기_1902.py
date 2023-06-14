n = int(input())

def plus(n):
    if n != 0:
        print(n)
        plus(n-1)

plus(n)