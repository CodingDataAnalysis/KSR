a, b, c, d, e, f = map(int, input().split())

n = a*e - b*d
x = c * (e) + f * (-b) 
y = c * (-d) + f * (a)

x = int(x / n)
y = int(y / n)

print(x, y)

