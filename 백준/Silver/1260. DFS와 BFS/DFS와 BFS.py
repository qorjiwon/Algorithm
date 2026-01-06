import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for li in graph:
    li.sort()

visited = [0]*(N+1)
visited[V]=1

def dfs(now):
    print(now, end=' ')
    for n in graph[now]:
        if not visited[n]:
            visited[n] = 1
            dfs(n)
dfs(V)
print()

q = [V]
visited = [0]*(N+1)
visited[V] = 1
while q:
    now = q.pop(0)
    print(now, end=' ')
    for n in graph[now]:
        if not visited[n]:
            visited[n] = 1
            q.append(n)
print()