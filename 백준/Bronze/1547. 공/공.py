m = int(input())
cup = [0 for _ in range(4)]
cup[1]=1
for _ in range(m):
    x, y = map(int, input().split())
    temp = cup[x]
    cup[x] = cup[y]
    cup[y] = temp
    
print(cup.index(1))