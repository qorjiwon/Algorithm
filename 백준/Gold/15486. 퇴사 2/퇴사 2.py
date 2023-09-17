import sys
input = sys.stdin.readline

N = int(input())
T, P = [0]*(N+1), [0]*(N+1)
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1) # dp[k] = k일까지 가능한 최댓값
for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1]) # 이전까지의 최댓값
    end_day = i+T[i]-1 # 상담 마지막 날
    if end_day <= N:
            dp[end_day] = max(dp[end_day], dp[i-1]+P[i])
print(max(dp))