import sys
from itertools import permutations

# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# op_lst = list(map(int, sys.stdin.readline().split()))

n = 3
a = list(map(int, "3 4 5".split()))
op_lst = list(map(int, "1 0 1 0".split()))
# lst = []

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def division(a, b):
    return a // b

# print()

op = ['+'] * op_lst[0] + ['-'] * op_lst[1] + ['*'] * op_lst[2] + ['//'] * op_lst[3]


cal = list(permutations(op, n-1))

def calculate(lst):
    first = a.pop()
    second = a[0]

    for i in range(len(lst)):
        if lst[i] == '+':
            a[i] = plus(first, second)
        elif lst[0] == '-':
            a[i] = minus(first, second)
        elif lst[0] == '*':
            a[i] = multiple(first, second)
        elif lst[0] == '//':
            a[i] = division(first, second)


for i in range(len(cal)):
    calculate(cal[i])
