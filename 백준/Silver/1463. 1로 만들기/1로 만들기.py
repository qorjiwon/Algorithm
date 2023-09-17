import sys
input = sys.stdin.readline

inf = 1e9
N = int(input())
dp = [0]*max(N+1,4)
dp[2] = 1
dp[3] = 1

for i in range(4,N+1):
    a = [i-1]
    if i%3 == 0:
        a.append(i//3)
    if i%2 == 0:
        a.append(i//2)
    dp[i] = min([dp[e] for e in a])+1
    
print(dp[N])