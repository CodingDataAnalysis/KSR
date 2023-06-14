a, b = map(int, input().split())

lst = []
def odd(a, b):
    if a % 2 != 0:
        lst.append(a)
    if a != b:
        odd(a+1, b)
    else:
        print(*lst)
odd(a, b)


