n = int(input())

for i in range(0, n):
    row = i + 1
    space = " " * (n - row)
    star = "*" * (2 * row - 1)
    print(space + star)

for i in range(n-1, 0, -1):
    row = i
    space = " " * (n - row)
    star = "*" * (2 * row - 1)
    print(space + star)