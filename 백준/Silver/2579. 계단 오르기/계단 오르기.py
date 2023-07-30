import sys
input = sys.stdin.readline

N = int(input())
if N < 4:
    stairs = [int(input()) for _ in range(N)]
    result = [0]*4
    for i in range(3-N):
        stairs.append(0)
else:
    stairs = [int(input()) for _ in range(N)]
    result = [0]*N
result[0] = stairs[0]
result[1] = stairs[0]+stairs[1]
result[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
for i in range(3,N):
    result[i] = max(result[i-3]+stairs[i-1]+stairs[i], stairs[i]+result[i-2])
print(result[N-1])