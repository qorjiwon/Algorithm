import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(input().rstrip()) for _ in range(N)]

result = 0
visited = [[0]*M for _ in range(N)]
dp = [[0]*M for _ in range(N)]

def dfs(x,y,d):
    X = int(m[x][y])
    dx = [X,0,-X,0]
    dy = [0,X,0,-X]
    ans = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx and nx < N and -1 < ny and ny < M and m[nx][ny] != 'H' and dp[nx][ny] < d+1:
            if visited[nx][ny]:
                print(-1)
                exit()
            visited[nx][ny]=1
            dp[nx][ny] = d+1
            ans.append(dfs(nx,ny, d+1))
            visited[nx][ny]=0
    if ans:
        return max(ans)
    return d+1
            
print(dfs(0,0,0))