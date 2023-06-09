
n = int(input())

def three(n):
    if n == 1:
        return n
    else:
        print(n)
        if n % 2 != 0:
            return three(3 * n + 1)
    
        elif n % 2 == 0:
            return three(n // 2)
    

print(three(n))

