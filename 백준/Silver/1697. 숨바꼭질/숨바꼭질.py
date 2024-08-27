from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([N])
arr = [-1]*100001
arr[N]=0
    
while q:
    x = q.popleft()
    if x == K:
        print(arr[x])
        break
    if x < K:
        nX = [x*2, x+1, x-1]
    else:
        nX = [x-1]
    for nx in nX:
        if 0 <= nx and nx <= 100000:
            if arr[nx] == -1:
                arr[nx] = arr[x] + 1
                q.append(nx)