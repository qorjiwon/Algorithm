import sys
input = sys.stdin.readline

n, m = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque
def bfs(i,j):
    q = deque([(i,j)])
    M[i][j]=0
    ans = 0
    while q:
        x, y = q.popleft()
        ans += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < n and -1 < ny and ny < m and M[nx][ny]:
                M[nx][ny]=0
                q.append((nx,ny))
    return ans
                
pictures = [0]
for i in range(n):
    for j in range(m):
        if M[i][j]:
            pictures.append(bfs(i,j))

print(len(pictures)-1)
print(max(pictures))