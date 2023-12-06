n = int(input())

lst = [i for i in range(1, n+1) if n % i == 0]
lst = lst[1:]

for i in lst:
    while n % i == 0:
        n = n // i
        print(i)
    
