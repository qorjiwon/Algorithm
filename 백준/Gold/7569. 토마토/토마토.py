import sys
input = sys.stdin.readline

M, N, H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

from collections import deque
result=0
q = deque()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][i][j] == 1:
                q.append((k,i,j,0))
while q:
    z,x,y,d=q.popleft()
    result = max(result,d)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if -1 < nx and nx < N and -1 < ny and ny < M and -1 < nz and nz < H and arr[nz][nx][ny]==0:
            q.append((nz, nx, ny, d+1))
            arr[nz][nx][ny]=1
                
for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][i][j] == 0:
                result = -1
print(result)