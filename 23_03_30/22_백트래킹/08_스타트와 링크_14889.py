import sys
from itertools import permutations
# n = int(sys.stdin.readline())

# lst = []
# for i in range(n):
#     lst.append(list(map(int, sys.stdin.readline().split())))

# lst = []
# def cal():
#     for i in range(n):
#         if len(lst)

lst = [1, 2, 3]
print(list(permutations(lst, 2)))