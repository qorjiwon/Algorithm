from collections import deque

def bfs(m, i, j, visited):
    queue = deque([[i, j]])
    t=0
    while queue:
        v = queue.popleft()
        t+=1
        visited[v[0]][v[1]]=1
        if v[0]-1 > -1 and visited[v[0]-1][v[1]]==0 and m[v[0]-1][v[1]]=='1':
            queue.append([v[0]-1, v[1]])
            visited[v[0]-1][v[1]]=1
        if v[1]-1 > -1 and visited[v[0]][v[1]-1]==0 and m[v[0]][v[1]-1]=='1':
            queue.append([v[0],v[1]-1])
            visited[v[0]][v[1]-1]=1
        if v[0]+1 < N and visited[v[0]+1][v[1]]==0 and m[v[0]+1][v[1]]=='1':
            queue.append([v[0]+1, v[1]])
            visited[v[0]+1][v[1]]=1
        if v[1]+1 < N and visited[v[0]][v[1]+1]==0 and m[v[0]][v[1]+1]=='1':
            queue.append([v[0], v[1]+1])
            visited[v[0]][v[1]+1]=1
    return t

N = int(input())
m = []
for _ in range(N):
    m.append(list(input()))

danzi=[]
visited=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j]==0 and m[i][j]=='1':
            danzi.append(bfs(m, i, j, visited))

print(len(danzi))
danzi.sort()
for i in danzi:
    print(i)