from collections import deque
M, N = map(int, input().split())

tomato=[]
tmt_count=0
all = M*N
for i in range(N):
    tomato.append(list(map(int, input().split())))
    tmt_count += tomato[i].count(1)
    all -= tomato[i].count(-1)

queue = deque()
day = 0
for i in range(N):
    for j in range(M):
        if(tomato[i][j] == 1):
            queue.append([i, j])

while tmt_count != all and len(queue) != 0:
    for _ in range(len(queue)):
        v = queue.popleft()
        if v[0] > 0 and tomato[v[0]-1][v[1]]==0:
            queue.append([v[0]-1, v[1]])
            tomato[v[0]-1][v[1]]=1
        if v[1] > 0 and tomato[v[0]][v[1]-1]==0:
            queue.append([v[0],v[1]-1])
            tomato[v[0]][v[1]-1]=1
        if v[0]+1 < N and tomato[v[0]+1][v[1]]==0:
            queue.append([v[0]+1, v[1]])
            tomato[v[0]+1][v[1]]=1
        if v[1]+1 < M and tomato[v[0]][v[1]+1]==0:
            queue.append([v[0], v[1]+1])
            tomato[v[0]][v[1]+1]=1
    tmt_count += len(queue)
    day+=1

if tmt_count != all:
    print(-1)
else:
    print(day)