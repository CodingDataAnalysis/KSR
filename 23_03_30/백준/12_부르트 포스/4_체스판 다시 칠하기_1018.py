import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(n):
    a = sys.stdin.readline().split()
    lst.append(a)

cnt = 0
first = lst[0][0]


for i in range(0, n):
    for j in range(0, m, 2):
        if first != lst[i][j]:
            cnt += 1

for i in range(1, n, 2):
    for j in range(1, m, 2):
        if first == lst[i][j]:
            cnt += 1

print(cnt)

