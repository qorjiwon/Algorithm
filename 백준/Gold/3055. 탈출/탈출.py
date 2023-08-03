import sys
input = sys.stdin.readline

R, C = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]

from collections import deque
q_rain = deque() #비가 올 예정
for i in range(R):
    for j in range(C):
        if m[i][j] == '*':
            q_rain.append((i,j))
        elif m[i][j] == 'D': # 동굴 위치
            D = (i,j)
        elif m[i][j] == 'S': # 고슴도치 초기 위치
            q_S = deque([(i,j)])
arrive = 0
result = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while q_S and not arrive:
    result += 1
    for _ in range(len(q_rain)):
        x, y = q_rain.popleft()
        m[x][y] = '*'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < R and -1 < ny and ny < C:
                if m[nx][ny] == '.' or m[nx][ny] == 'S':
                    q_rain.append((nx,ny))
                    m[nx][ny] = '*'
    for _ in range(len(q_S)):
        x, y = q_S.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < R and -1 < ny and ny < C:
                if m[nx][ny] == '.': # 빈 땅이면
                    q_S.append((nx,ny))
                    m[nx][ny]='S'
                elif m[nx][ny] == 'D': # 동굴일 때
                    arrive = 1
                    break
                
if arrive:
    print(result)
else:
    print('KAKTUS')