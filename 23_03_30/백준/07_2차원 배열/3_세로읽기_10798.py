import sys

lst = []
max_len = []
for i in range(5):
    a = sys.stdin.readline().strip()
    lst.append(list(a))
    max_len.append(len(a))

text = ''
for i in range(max(max_len)):
    for j in range(5):
        try:
            text = text + ''.join(lst[j][i])
        except:
            pass


print(text)


'''
(1, 1) 1 
(2, 1) 1
(3, 1) 1
(1, 2) 1

(1, 1) 2


'''