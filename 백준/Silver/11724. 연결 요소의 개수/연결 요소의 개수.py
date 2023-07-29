import sys
input = sys.stdin.readline

N, M = map(int,input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
    
from collections import deque
def bfs(start, visited):
    q=deque([start])
    while q:
        x = q.popleft()
        for e in edges[x]:
            if visited[e]==0:
                q.append(e)
                visited[e]=1
    
visited = [0]*(N+1)
result = 0
for i in range(N):
    if visited[i]==0:
        result += 1
        bfs(i, visited)
print(result)