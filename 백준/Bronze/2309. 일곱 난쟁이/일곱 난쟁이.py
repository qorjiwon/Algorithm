a = [int(input()) for _ in range(9)]
find = 0
for i in range(8):
    for j in range(i+1, 9):
        if sum(a)-a[i]-a[j] == 100:
            a.pop(j)
            a.pop(i)
            a.sort()
            find = 1
            for elem in a:
                print(elem)
            break
    if find: break