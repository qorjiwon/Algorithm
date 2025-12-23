import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
connection = [[] for _ in range(n+1)]
infected = [0] * (n+1)
infected[1] = 1
q = deque([1])
for _ in range(int(input())):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

while q:
    x = q.pop()
    for i in connection[x]:
        if not infected[i]:
            infected[i] = 1
            q.append(i)

print(sum(infected)-1)