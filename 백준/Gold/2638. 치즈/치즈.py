import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = [(0, 0)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = -1

while q:
    _q = []
    while q:
        x, y = q.pop()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                v = arr[nx][ny]
                if v < 0:
                    continue
                elif not v:
                    arr[nx][ny] = -1
                    q.append((nx, ny))
                elif v == 1:
                    arr[nx][ny] += 1
                else:
                    arr[nx][ny] = -1
                    _q.append((nx, ny))
    q = _q
    ans += 1

print(ans)