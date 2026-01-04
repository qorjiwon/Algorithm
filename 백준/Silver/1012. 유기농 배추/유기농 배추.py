import sys
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        Y, X = map(int, input().split())
        arr[X][Y] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                ans += 1
                q = [(i, j)]
                while q:
                    x, y = q.pop()
                    for (dx, dy) in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]:
                            q.append((nx, ny))
                            arr[nx][ny] = 0
    print(ans)