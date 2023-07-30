import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
mymap = [[0]*(N) for _ in range(N)]
mymap[0][0]=1
for x in range(N):
    for y in range(N):
        n = m[x][y]
        dx = [n,0]
        dy = [0,n]
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < N and ny < N:
                    mymap[nx][ny] += mymap[x][y]
#위에 이중 for문에서 x=y=N-1일 때 자기 자신을 두 번 더하는 것 때문에 나누어줌
#                                               1->2배->4배
print(mymap[N-1][N-1]//4)