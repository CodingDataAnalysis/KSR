import sys

a = []
b = []
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)

def cnt(lst):
    for i in list(set(lst)):
        if lst.count(i) == 1:
            p = i

    return p

print(cnt(a), cnt(b))