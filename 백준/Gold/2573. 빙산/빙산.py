import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int,input().split())) for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
    
from collections import deque
def bfs(x, y): # 이어진 빙산 모두 0으로 만들기
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < N and -1 < ny and ny < M and tmp_m[nx][ny]:
                tmp_m[nx][ny] = 0
                q.append((nx,ny))
                
total_ice = 0
for a in m:
    for b in a:
        if b:
            total_ice += 1
year = 0
tmp_m = [[x for x in e] for e in m]
while total_ice:
    p = 0
    for x in range(N):
        for y in range(M):
            if tmp_m[x][y]:
                p += 1
                bfs(x,y)
    if p > 1:
        print(year)
        exit()
    tmp_m = [[x for x in e] for e in m]
    for x in range(N):
        for y in range(M):
            if m[x][y]:
                 for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if -1 < nx and nx < N and -1 < ny and ny < M:
                        if not m[nx][ny] and tmp_m[x][y]:
                            tmp_m[x][y] -= 1
                            if tmp_m[x][y] == 0:
                                total_ice -= 1
    m = [[x for x in e] for e in tmp_m]
    year += 1
print(0)