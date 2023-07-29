import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr=[[0]*(M) for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1]=1
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque
q = deque()
def bfs(x, y):
    q.append((x,y))
    arr[x][y]=0
    ans = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < N and -1 < ny and ny < M and arr[nx][ny]==1:
                q.append((nx,ny))
                arr[nx][ny]=0
                ans += 1
    return ans

result = 0
for j in range(M):
    for i in range(N):
        if arr[i][j]==1:
            result = max(result, bfs(i,j))
            
print(result)