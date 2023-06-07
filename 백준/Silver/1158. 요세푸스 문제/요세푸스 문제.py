from collections import deque
N, K = map(int,input().split())

q = deque()
for i in range(1,N+1):
    q.append(str(i))

print('<',end='')
for _ in range(N-1):
    for _ in range(K-1):
        q.append(q.popleft())
    print(q.popleft()+', ',end='')
print(q.pop()+'>')