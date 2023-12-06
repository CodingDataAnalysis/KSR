
a = int(input())

n = 0
for i in range(1, a+1):
    b = list(map(int, str(i)))
    n = i + sum(b)
    if n == a:
        print(i)
        break

    elif i == a:
        print(0)




# map 사용

'''
from itertools import product

a = input()
n = len(a)

lst = [i for i in range(10)]
pmt = list(product(lst, repeat = n))

new = []
for i in range(len(pmt)):
    text = ''
    lstt = [str(pmt[i][j]) for j in range(len(pmt[i]))]
    text = ''.join(lstt)
    text = int(text)

    if sum(pmt[i]) + text == int(a):
        new.append(text)

if new:
    print(min(new))

else:
    print(0)

# map 사용


'''