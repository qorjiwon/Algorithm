import sys
input = sys.stdin.readline

A, B = map(int, input().split())
n = 1
while A < B:
    if B%2 == 0:
        B = B//2
    elif B%10 == 1:
        B = B//10
    else:
        B = -1
    n += 1
if A == B:
    print(n)
else:
    print(-1)