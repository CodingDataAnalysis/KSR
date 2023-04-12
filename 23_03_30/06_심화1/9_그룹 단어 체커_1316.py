
n = int(input())

cnt = 0

for i in range(n):
    a = input()
    a = [a[i] for i in range(len(a))]
    a_set = list(set(a))


    for j in range(len(a_set)):

        if len(a_set) == 0:
            break
        elif a_set[0] == a[0]:
            a = a[1:]
            a_set = a_set[1:]
        elif a_set[0] != a[0]:
            a_set = a_set[1:]
        
    cnt += 1

# find <- index 찾아줌



print(cnt)




n = int(input())

cnt = 0

for i in range(n):
    a = input()
    a = [a[i] for i in range(len(a))]
    a_set = list(set(a))

    
    if a_set != a:
        if len(a_set) == 1:
            cnt += 1
        else:
             pass

    elif a_set == a:
            cnt += 1

print(cnt)



    # if a_set != a:
    #     if a_set[0] == a[-1] and a_set[0] == a[0]:
    #         cnt += 1
    #         print(a_set, a, "!=")
    #     else:
    #          pass

    # elif a_set == a:
    #         cnt += 1
    #         print(a_set, a, "==")

    # for j in range(len(a_set)):
    #     for k in range(len(a)):