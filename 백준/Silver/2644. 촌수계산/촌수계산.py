from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
q = deque()

rel = [[] for _ in range(n+1)] # relationship
for i in range(m):
    x, y = map(int, input().split())
    rel[x].append(y)
    rel[y].append(x)
visited = [0]*(n+1)

ans = -1

for i in rel[a]:
    visited[i] = 1
    q.append([i, 1])

while q:
    x, cnt = q.popleft()
    if (x == b):
        ans = cnt
        break
    for i in rel[x]:
        if (visited[i] == 0):
            visited[i] = 1
            q.append([i, cnt+1])

print(ans)