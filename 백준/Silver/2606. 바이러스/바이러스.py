import sys
input = sys.stdin.readline

n = int(input())
connection = [[] for _ in range(n+1)]
infected = [0] * (n+1)
infected[1] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

def dfs(x):
    for i in connection[x]:
        if not infected[i]:
            infected[i] = 1
            dfs(i)

dfs(1)
print(sum(infected)-1)