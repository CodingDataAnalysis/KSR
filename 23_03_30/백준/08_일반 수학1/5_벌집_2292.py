'''

1: 1
2 3 4 5 6 7 : 6
8 9 10 11 12 13 14 15 16 17 18 19 : 12
18
'''

# a = int(input())
a = 20
min = 1
cnt = 0

while a > min:
    cnt += 1
    min = min + 6 * cnt
print(cnt + 1)