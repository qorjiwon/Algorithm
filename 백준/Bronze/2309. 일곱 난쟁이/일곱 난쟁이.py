a = [int(input()) for _ in range(9)]

find = i =0
while not find:
    for j in range(i+1, 9):
        if sum(a)-a[i]-a[j] == 100:
            a.pop(j)
            a.pop(i)
            a.sort()
            find = 1
            for elem in a:
                print(elem)
            break
    i += 1