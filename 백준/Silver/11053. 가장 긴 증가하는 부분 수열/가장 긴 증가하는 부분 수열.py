import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1]*N
for i in range(N):
    m = A[i]
    for k in range(i-1,-1,-1):        
        if m > A[k]:
            dp[i] = max(dp[i], dp[k]+1)
print(max(dp))