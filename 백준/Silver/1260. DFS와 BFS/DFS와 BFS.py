N, M, V = map(int, input().split())

graph=[[] for i in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, N+1):
    graph[i].sort()

visited=[0]*(N+1)

def dfs(graph, v, visited):
    visited[v]=1
    print(v, end=' ')
    for i in graph[v]:
        if(visited[i] == 0):
            dfs(graph, i, visited)

dfs(graph, V, visited)
print()
###########################################################
from collections import deque

visited=[0]*(N+1)

def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        visited[v]=1
        print(v, end=' ')
        for i in graph[v]:
            if (visited[i]==0):
                visited[i]=1
                queue.append(i)
bfs(graph, V, visited)