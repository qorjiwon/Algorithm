from collections import deque
import sys

input = sys.stdin.readline
dx = [-1,-2,-2,-1,+1,+2,+2,+1]
dy = [-2,-1,+1,+2,-2,-1,+1,+2]

for _ in range(int(input())):
    l = int(input())
    m = [[0]*l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    ans = 0
    q = deque([(start_x, start_y)])
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            print(m[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < l and -1 < ny and ny < l and not m[nx][ny]:
                m[nx][ny] = m[x][y] + 1
                q.append((nx,ny))