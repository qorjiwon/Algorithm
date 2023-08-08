import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

for c in list(combinations(range(1,N+1),M)):
    print(*c)