import sys
input = sys.stdin.readline

N, M = map(int,input().split())

from collections import deque
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

bacon = []
q = deque()
for i in range(1,N+1):
    visited = [0]*(N+1)
    visited[i]=-1
    q.append((i,0))
    while q:
        x, d = q.popleft()
        for e in arr[x]:
            if visited[e]==0:
                visited[e]=d+1
                q.append((e,d+1))
    bacon.append(sum(visited)+1)                
b = min(bacon)
print(bacon.index(b)+1)