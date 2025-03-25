import sys
input = sys.stdin.readline

A = []
B = []

N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(K):
        print(sum([A[i][k] * B[k][j] for k in range(M)]), end=' ')
    print()