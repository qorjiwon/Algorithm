from collections import deque
import sys
input = sys.stdin.readline

F, G, S, U, D = map(int, input().split())

q = deque([[G,0]])
visited = [0] * (F + 1)

ans = "use the stairs"
while q:
    cur, n = q.popleft()
    if cur == S:
        ans = n
        break
    for next in [cur + U, cur - D]:
        if 0 < next and next <= F and not visited[next]:
            visited[next] = 1
            q.append([next, n + 1])
print(ans)