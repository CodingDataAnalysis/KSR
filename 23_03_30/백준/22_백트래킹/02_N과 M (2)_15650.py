import sys
from itertools import combinations

# m, n = map(int, sys.stdin.readline().split())


# lst = [i for i in range(1, m + 1)]

# answer = list(combinations(lst, n))

# for i in answer:
#     print(*i)


m = 4
n = 2

lst = []

def cal(a):
    if len(lst) < n:
        for i in range(a, m+1):
            lst.append(i)
            cal(i+1)
            lst.pop()

    else:
        print(*lst)

cal(1)
