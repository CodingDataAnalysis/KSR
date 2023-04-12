import sys

n = int(sys.stdin.readline())
window = [0] * (n + 1)

lst = []
def number(num):
    for i in range(0, n, num):
        a = i + num
        try:
            if window[a] == 0:
                window[a] = 1
            elif window[a] == 1:
                window[a] = 0

        except:
            pass


for i in range(1, n + 1):
    number(i)

window = window[1:]
print(window.count(1))

