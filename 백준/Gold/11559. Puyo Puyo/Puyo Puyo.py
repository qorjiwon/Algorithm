import sys
input = sys.stdin.readline

m = [list((input().rstrip())) for _ in range(12)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque
def bfs(puyo, x,y):
    a = [(x,y)]
    m[x][y]='.'
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < 12 and -1 < ny and ny < 6:
                if m[nx][ny] == puyo:
                    a.append((nx,ny))
                    q.append((nx,ny))
                    m[nx][ny] = '.'
    if len(a) < 4:
        for e in a:
            x, y = e
            m[x][y] = puyo
        return 0
    return len(a)
        
bang = 0
cnt = 0
while 1:
    bang = 0
    for i in range(11,-1,-1):
        for j in range(5,-1,-1):
            if m[i][j] != '.':
                bang += bfs(m[i][j], i,j)
    if bang==0: # 안터졌으면 탈츨
        break
    else: # 터졌으면 뿌요 내리기
        for j in range(6):
            for i in range(11,0,-1):
                if m[i][j] == '.' and m[i-1][j] != '.':
                    d = i-1
                    while d < 11 and m[d+1][j] == '.':
                        m[d+1][j] = m[d][j]
                        m[d][j]='.'
                        d += 1
        cnt += 1
print(cnt)