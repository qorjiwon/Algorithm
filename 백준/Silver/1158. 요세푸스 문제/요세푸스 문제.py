from collections import deque
import sys

N, K = map(int,sys.stdin.readline().split())

q = deque()
for i in range(1,N+1):
    q.append(str(i))

print('<',end='')
for _ in range(N-1):
    for _ in range(K-1):
        q.append(q.popleft())
    print(q.popleft()+', ',end='')
print(q.pop()+'>')