

# while True:
#     try:
#         text = '-'
#         n = int(input())
#         for j in range(n):
#             text = text + ' ' * n**j + text
#             # text = text + text[::-1]
#         print(text)
#     except:
#         break


def cantor(num, text):
    space = num // 3
    text = text[:space] + ' ' * space + text[space*2:]
    print(text)
    cantor()


n = 3
num = 3 ** n
text = '-' * (3**n)
cantor(num, text)

'''
123456789
123***789
1*3***7*9
012345678

'''
