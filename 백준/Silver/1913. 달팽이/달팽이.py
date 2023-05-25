n=int(input())

dal = [[0 for _ in range(n)] for _ in range(n)]

item = 1
x= n//2
y = n//2
for i in range(1, n+1, 2):
    if (i == 1):
        dal[y][x] = item
        item += 1
    else:
        y -= 1
        dal[y][x] = item
        item += 1
        for _ in range(i-2):
            x += 1
            dal[y][x] = item
            item += 1
        for _ in range(i-1):
            y += 1
            dal[y][x] = item
            item += 1
        for _ in range(i-1):
            x -= 1
            dal[y][x] = item
            item += 1
        for _ in range(i-1):
            y -= 1
            dal[y][x] = item
            item += 1

m = int(input())
for i in range(n):
    for j in range(n):
        if (dal[i][j] == m):
            break
    if (dal[i][j] == m):
            i += 1
            j += 1
            break
for a in dal:
    for b in a:
        print(b, end=' ')
    print()
    
print(i, j)