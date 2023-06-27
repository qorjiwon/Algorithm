import sys
input = sys.stdin.readline
inf = int(1e9)

N, E = map(int,input().split())

graph = [[] for _ in range(N+1)]

dist1 = [inf]*(N+1)
dist2 = [inf]*(N+1)
dist3 = [inf]*(N+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def get_smallest_node(distance, visited):
    min_value = inf
    index = 0
    for i in range(1,N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start,distance):
    distance[start]=0
    visited = [0 for _ in range(N+1)]
    visited[start]=1
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(N-1):
        now = get_smallest_node(distance, visited)
        visited[now] = 1
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
v1, v2 = map(int, input().split())
dijkstra(1, dist1)
dijkstra(v1, dist2)
dijkstra(v2, dist3)

result = min(dist1[v1]+dist2[v2]+dist3[N], dist1[v2]+dist3[v1]+dist2[N])

if result >= inf:
    print(-1)
else:
    print(result)