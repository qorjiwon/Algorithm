N = int(input()) # 도시 수
M = int(input()) # 여행 계획에 속한 도시 수

m = [] # 도시의 연결 정보. 1이면 연결된 것.
for _ in range(N):
    m.append(list(map(int, input().split())))
    
b = list(map(int, input().split()))

from collections import deque

for i in range(N):
    m[i][i]=1

def bfs(m, start, end, visited):
    queue = deque()
    visited[start-1] = 1
    if m[start-1][end-1] == 1 :
        return 1
    else:
        for i in range(N):
            if m[start-1][i] == 1 and visited[i] == 0:
                queue.append(i+1)
                visited[i] = 1
        r = 0
        while queue and r == 0:
            t = queue.popleft()
            r = bfs(m, t, end, visited)
        return r

for i in range(M-1):
    visited = [0]*N
    result = bfs(m, b[i], b[i+1], visited)
    if result == 0:
        break
    
if result == 0:
    print('NO')
else:
    print('YES')
    