import sys

basket, num = map(int, sys.stdin.readline().split())

arr = [i+1 for i in range(basket)]

lst = []
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    a = a - 1
