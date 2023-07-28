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
            if e not in visited:
                q.append(e)
                visited.append(e)
    
    
visited = []
result = 0
for i in range(N):
    if i not in visited:
        result += 1
        bfs(i, visited)
print(result)