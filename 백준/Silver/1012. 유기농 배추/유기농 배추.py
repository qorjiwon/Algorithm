import sys
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cabbages = set()
    for _ in range(K):
        Y, X = map(int, input().split())
        cabbages.add((X, Y))
    ans = 0
    while cabbages:
        ans += 1
        q = [cabbages.pop()]
        while q:
            x, y = q.pop()
            for (dx, dy) in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) in cabbages:
                    cabbages.discard((nx, ny))
                    q.append((nx, ny))
            
    print(ans)