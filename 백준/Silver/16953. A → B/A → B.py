import sys
input = sys.stdin.readline

A, B = map(int, input().split())
from collections import deque
q = deque([(A,0)])
while q:
    a, n = q.popleft()
    if a < B:
        q.append((a*2,n+1))
        q.append((int(str(a)+'1'),n+1))
    elif a == B:
        print(n+1)
        exit()
print(-1)