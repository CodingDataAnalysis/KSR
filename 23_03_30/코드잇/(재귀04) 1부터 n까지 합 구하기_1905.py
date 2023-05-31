n = 100

def plus(n):
    if n != 0:
        plus(n-1)
    else:
        answer = 0
    
    answer += n


print(plus(n))

'''
100

'''


