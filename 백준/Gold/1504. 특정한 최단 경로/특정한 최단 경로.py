import sys
input = sys.stdin.readline
inf = 800*200000

N, E = map(int,input().split())

graph = [[] for _ in range(N+1)]

dist1 = [inf]*(N+1)
dist2 = [inf]*(N+1)
dist3 = [inf]*(N+1)

for _ in range(E): # 간선 추가
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def get_smallest_node(distance, visited): # 방문하지 않는 노드 중 가장 가까운 노드의 인덱스 반환
    min_value = inf
    index = 0
    for i in range(1,N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start,distance): #start에서 각 노드까지의 최단 거리 반환
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

# 경유 노드 순서에 따라서 dist 순서 바꿔줘야 되는거 잊지 말기
result = min(dist1[v1]+dist2[v2]+dist3[N], dist1[v2]+dist3[v1]+dist2[N])

if result >= inf:
    print(-1)
else:
    print(result)