import sys
import math

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)

distance = []
for i in range(len(lst) - 1):
    b = lst[i+1] - lst[i]
    distance.append(b)

for i in range(0, len(distance) - 1):
    g = math.gcd(distance[i], distance[i+1])

new = [lst[0]]

a = lst[0]
for i in range(lst[0], lst[-1]):
    if a >= lst[-1]:
        break
    else:
        a = a + g
        new.append(a)
print(len(new) - len(lst))