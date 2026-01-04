from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dx = [-1, 1, 0, 0]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
for li in arr:
    if 1 in li:
        q.append((0, 0))
        break

while q:
    visited = [[0] * M for _ in range(N)]
    while q:  # 치즈 녹을 곳 검사
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny]:
                    arr[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    for i in range(N):  # 치즈 녹이기
        for j in range(M):
            if arr[i][j] > 2:
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 1
    ans += 1
    for li in arr:
        if 1 in li:
            q.append((0, 0))
            break
print(ans)