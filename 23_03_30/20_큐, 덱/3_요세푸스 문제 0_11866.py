import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
c = b - 1
lst = [i for i in range(1, a+1)]
new = []

while len(lst) != 0:
    try:
        if c < len(lst):
            new.append(lst.pop(c))
            c += b - 1
        else:
            c = c - len(lst)
            new.append(lst.pop(c))
            c += b - 1
    except:
        continue

print("<" + ', '.join(str(i) for i in new) + ">")


'''

1 2 3 4 5 6 7 c = 2
3 / 1 2 4 5 6 7 c = 4
6 / 1 2 4 5 7 c = 6
2 / 1 4 5 7



2, 5, 1, 4, 0, 3, 6
'''