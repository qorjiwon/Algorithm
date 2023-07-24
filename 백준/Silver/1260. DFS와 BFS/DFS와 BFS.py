import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(N+1):
    graph[i].sort()

def dfs(start, visited):
    visited[start]=1
    print(start, end=' ')
    for e in graph[start]:
        if visited[e] == 0:
            dfs(e, visited)
    
from collections import deque

def bfs(visited, q):
    while q:
        x = q.popleft()
        print(x, end=' ')
        for e in graph[x]:
            if visited[e] == 0:
                q.append(e)
                visited[e]=1
    
visited = [0]*(N+1)
dfs(V, visited)
print()
q = deque([V])
visitedd = [0]*(N+1)
visitedd[V]=1
bfs(visitedd, q)