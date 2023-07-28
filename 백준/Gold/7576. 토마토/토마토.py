import sys
input = sys.stdin.readline

M, N = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

from collections import deque
q = deque()
for i in range(N):
    for j in range(M):
        if m[i][j] == 1:
            q.append((i,j,0))
            
ans = 0
while q:
    x,y,d = q.popleft()
    ans = max(ans, d)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx and nx < N and -1 < ny and ny < M and m[nx][ny]==0:
            q.append((nx,ny, d+1))
            m[nx][ny]=1

for i in range(N):
    for j in range(M):
        if m[i][j]==0:
            ans=-1
print(ans)