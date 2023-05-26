C = int(input())
SS = int(input())

graph=[[] for i in range(C+1)]
#print(graph)
for i in range(SS):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

visited=[0]*(C+1)
#print(graph)

def dfs(graph, v, visited):
    visited[v]=1
    for i in graph[v]:
        if(visited[i] == 0):
            dfs(graph, i, visited)

dfs(graph, 1, visited)
#최초 감염 컴퓨터 제외
print(visited.count(1)-1)