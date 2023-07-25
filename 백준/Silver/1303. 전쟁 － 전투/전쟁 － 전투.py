import sys
input = sys.stdin.readline

M, N = map(int, input().split())
men = [list(input()) for _ in range(N)]

from collections import deque

q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
    
def bfs(x,y,k):
    men[x][y]=0
    q = deque([(x,y)])
    ans = 1
    while q:
        n = q.popleft()
        x = n[0]
        y = n[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < N and -1 < ny and ny < M and men[nx][ny] == k:
                q.append((nx,ny))
                men[nx][ny] = 0
                ans += 1
    return ans**2
        
W = 0
B = 0
for i in range(N):
    for j in range(M):
        if men[i][j] != 0:
            if men[i][j] == 'W':
                W += bfs(i,j,'W')
            if men[i][j] == 'B':
                B += bfs(i,j,'B')
                
print(W,B)