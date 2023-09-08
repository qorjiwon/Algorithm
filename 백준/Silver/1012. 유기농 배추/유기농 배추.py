import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]
    
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    m = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        m[Y][X] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if m[i][j]:
                ans += 1
                m[i][j]=0
                q = deque([(i,j)])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if -1 < nx and nx < N and -1 < ny and ny < M and m[nx][ny]:
                            m[nx][ny]=0
                            q.append((nx,ny))
    print(ans)
        
    