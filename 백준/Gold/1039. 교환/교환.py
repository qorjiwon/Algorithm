import sys
input = sys.stdin.readline

N, K = input().split()
K = int(K) ; M = len(N) ; N = tuple(N)

if M == 1: print(-1) ; exit()
if M == 2 and N[1]=='0': print(-1) ; exit()
arr = [N]
from itertools import combinations
for _ in range(K):
    T = set()
    dic = list(combinations(range(M),2))
    for n in arr:
        for a, b in dic:
            newn = list(n)
            newn[a], newn[b] = newn[b], newn[a]
            T.add(tuple(newn))
    arr = sorted(list(T))
print(''.join(arr[-1]))