import sys
input = sys.stdin.readline
inf = int(1e9)

n=int(input())
m=int(input())

result=[[inf]*n for _ in range(n)]

for i in range(n):
    result[i][i]=0

for _ in range(m):
    a, b, c = map(int,input().split())
    result[a-1][b-1] = min(result[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            result[i][j] = min(result[i][j], result[i][k]+result[k][j])
            
for i in range(n):
    for j in range(n):
        if result[i][j] == inf:
            result[i][j]=0

            
for x in result:
    print(*x)