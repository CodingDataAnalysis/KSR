import sys

n, k = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()
a = [int(a[i]) for i in range(len(a))]


def merge_a(a):
    if len(a) == 1:
        return a

    div = (len(a) // 2) + 1
    # len = 5 -> 2, 3
    left = a[0:div]
    right = a[div:]

    i, j = 0, 0
    lst2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst2.append(left[i])
            i += 1

        else:
            lst2.append(right[j])
            j += 1

    while i < len(left):
        
    

def sort_a(left, right):
    merge_a(left)
    merge_a(right)

'''
4 5 1 3 2
4 5 / 1 3 2
left / right
4 / 5 | 1 / 3 2
l / r | l / r




'''