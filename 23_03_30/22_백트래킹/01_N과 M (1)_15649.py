import sys
# from itertools import permutations

# m, n = map(int, sys.stdin.readline().split())

# lst = [i for i in range(1, m + 1)]

# answer = list(permutations(lst, n))

# for i in answer:
#     print(*i)


m = 2
n = 3

lst = []

def cal(m):
    if len(lst) < n:
        for i in range(1, m+1):
            if i not in lst:
                lst.append(i)
                cal(m-1)
                lst.pop()
    else:
        print(*lst)
cal(m)