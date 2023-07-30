import sys
input = sys.stdin.readline

N = int(input())
traffic = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
q=deque([([0,i],1,traffic[0][i]) for i in range(1,N) if traffic[0][i] != 0])
distance = []
while q:
    arr, n, d = q.popleft()
    if n == N-1:
        last = arr[n]
        if traffic[last][0] != 0:
            distance.append(d+traffic[last][0])
    else:
        s = arr[n]
        for i in range(1,N):
            if i not in arr and traffic[s][i] != 0:
                q.append((arr+[i],n+1, d+traffic[s][i]))
print(min(distance))