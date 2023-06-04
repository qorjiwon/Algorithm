N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

from collections import deque

result = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append(j)
            result[i][j]=1
    while queue:
        v = queue.popleft()
        for j in range(N):
            if graph[v][j] == 1 and result[i][j] == 0:
                queue.append(j)
                result[i][j] = 1

for a in result:
    print(' '.join(map(str,a)))