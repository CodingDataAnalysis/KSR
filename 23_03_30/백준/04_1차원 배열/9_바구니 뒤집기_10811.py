import sys

basket, num = map(int, sys.stdin.readline().split())

arr = [i+1 for i in range(basket)]


for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    a = a - 1

    arr[a:b] = list(reversed(arr[a:b]))
    arr = arr[:a] + arr[a:b] + arr[b:]

print(*arr)
