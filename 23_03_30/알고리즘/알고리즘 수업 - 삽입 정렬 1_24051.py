# A, N = map(int, input())
# k = list(map(int, input().split()))
num = '4 5 1 3 2'
k = list(map(int, num.split()))


def num_sort(lst):
    new = []
    for i in range(1, len(lst)):
        mem = k[i]
        for j in range(i, 0, -1):

            if lst[j-1] > mem:
                lst[j-1] = lst[j]
        
            else:
                lst[i+1] = mem
                break



    return lst

print(num_sort(k))


'''
4 5 1 3 2
4 5 5 3 2
k-1 k k+1


'''


