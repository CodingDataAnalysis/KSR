n = int(input())

f = [0] * 201
f[0] = 1
f[1] = 1

def fibo(n):
    if f[n-1] != 0:
        return f[n-1]
    
    else:
        f[n-1] = (fibo(n-1) + fibo(n-2)) % 10009
        return f[n-1]

print(fibo(n) % 10009)