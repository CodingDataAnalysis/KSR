# 10개 바구니 5번 회전
# 1번째 바구니~6번째 바구니 회전, 4번째 기준
# 1 2 3 4 5 6
# 4 5 6 1 2 3 


import sys
a, b = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, a+1)]

for i in range(b):
    x, y, z = map(int, sys.stdin.readline().split())
    
    x = x - 1
    z = z - 1

    lst = lst[:x] + lst[z:y] + lst[x:z] + lst[y:] 

print(*lst)