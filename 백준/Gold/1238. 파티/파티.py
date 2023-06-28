from heapq import heappush, heappop
import sys
input = sys.stdin.readline
inf=int(1e9)

N, M, X = map(int, input().split()) #마을과 학생 수, 간선 수, 파티 장소
graph = [[] for _ in range(N+1)]

for _ in range(M): # 간선 추가
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start, distance):
    q =[]
    visited = [0]*(N+1)
    visited[start]=1
    distance[start]=0
    for i in graph[start]:
        distance[i[0]]=i[1]
    for i in range(1,N+1):
        heappush(q, (distance[i], start, i))
    while q:
        v = heappop(q)
        if visited[v[2]]==1:
            continue
        else:
            visited[v[2]]=1
            for j in graph[v[2]]:
                cost = distance[v[2]]+j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
                    heappush(q,(cost, v[2], j[0]))
                    
dist=[inf]*(N+1)
dijkstra(X, dist)
distt = [inf]*(N+1)
dijkstra(1, distt)
result = distt[X]+dist[1]

for i in range(2,X):
    disttt = [inf]*(N+1)
    dijkstra(i,disttt)
    result = max(result, disttt[X]+dist[i])
    
for i in range(X+1,N+1):
    disttt = [inf]*(N+1)
    dijkstra(i,disttt)
    result = max(result, disttt[X]+dist[i])
    
print(result)