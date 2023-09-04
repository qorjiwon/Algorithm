import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min((M+1)//2,4))
elif M < 5:
    print(M)
elif M == 5:
    print(4)
else:
    print(M-2) # M-6+4