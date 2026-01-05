import sys
input = sys.stdin.readline

N, M = map(int, input().split())
room = [[*map(int, input().split())] for _ in range(N)]

d = [(-1, 0), (0, -1), (-1, -1)]
for x in range(N):
    for y in range(M):
        candies = [room[x][y]]
        for (dx, dy) in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny]:
                candies.append(room[x][y]+room[nx][ny])
        room[x][y] = max(candies)
print(room[N-1][M-1])