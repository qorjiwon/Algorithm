import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
q = deque([])

arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j, 0))
            arr[i][j] = 0
            ans[i][j] = 0


while q:
    x, y, d = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if -1 < nx < n and -1 < ny < m and arr[nx][ny]:
            arr[nx][ny] = 0
            ans[nx][ny] = d+1
            q.append((nx, ny, d+1))

# 갈 수 없는 땅 체크
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            ans[i][j] = -1

for li in ans:
    print(*li)