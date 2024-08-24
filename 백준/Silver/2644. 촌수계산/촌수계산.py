from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
queue = deque()

rel = [[] for _ in range(n+1)] # relationship
for i in range(m):
    x, y = map(int, input().split())
    rel[x].append(y)
    rel[y].append(x)
visited = [0]*(n+1)

ans = -1

for i in rel[a]:
    visited[i] = 1
    queue.append([i, 1])

while queue:
    x, cnt = queue.popleft()
    if (x == b):
        ans = cnt
        break
    for i in rel[x]:
        if (visited[i] == 0):
            visited[i] = 1
            queue.append([i, cnt+1])

print(ans)