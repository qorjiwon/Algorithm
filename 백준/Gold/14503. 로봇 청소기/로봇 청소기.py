from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

# 북서쪽(0,0), 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0 # 로봇 청소기가 청소하는 칸의 개수
m = [list(map(int, input().split())) for _ in range(N)]

while 0 <= r < N and 0 <= c < M and m[r][c] != 1: # 안이면서 벽이 아닌 경우
    if not m[r][c]: # 현재 칸이 청소되어 있지 않은 경우
        m[r][c] = 2 # 현재 칸 청소
        ans += 1
    isthere = 0 # 주변에 청소할 공간이 있는지 확인
    for i in range(4): 
        nd = (d + 3*i + 3) % 4 # 반시계 방향으로 회전
        nx = r + dx[nd]
        ny = c + dy[nd]
        if -1 < nx < N and -1 < ny < M and not m[nx][ny]: # 청소할 공간이 있는지
            isthere = True
            d = nd
            break
    if not isthere: # 주변에 청소할 공간이 없는 경우
        nd = (d + 2) % 4 # 후진
        r = r + dx[nd]
        c = c + dy[nd]
    else:
        r = r + dx[d]
        c = c + dy[d]
print(ans)