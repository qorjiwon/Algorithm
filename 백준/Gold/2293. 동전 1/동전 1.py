n, k = map(int, input().split())
c = [int(input()) for _ in range(n)] # 코인 종류
dp = [0]*(k+1) # dp[k] = 합이 k원이 되는 경우의 수
dp[0] = 1 # 동전을 1개만 쓸 때의 경우의 수 업데이트를 위해

for i in c:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[k])