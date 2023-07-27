import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int,input().rstrip())) for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

from collections import deque
def bfs(x,y):
    q = deque([(x,y)])
    m[x][y]=0
    ans=1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < N and -1 < ny and ny < N and m[nx][ny]==1:
                q.append((nx,ny))
                m[nx][ny]=0
                ans += 1
    return ans

result = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            result.append(bfs(i, j))
            
print(len(result))
result.sort()
for e in result:
    print(e)
