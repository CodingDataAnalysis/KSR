# 10개 바구니 5번 회전
# 1번째 바구니~6번째 바구니 회전, 4번째 기준
# 1 2 3 4 5 6
# 4 5 6 1 2 3 

a = 10
b = 5
i = 1
j = 6
k = 4

lst = [i for i in range(1, a+1)]

for num in lst:
    print(lst[j-i+1])
    