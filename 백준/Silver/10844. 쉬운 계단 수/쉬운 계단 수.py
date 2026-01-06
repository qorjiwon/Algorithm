N = int(input())
dp = [[0,1,1,1,1,1,1,1,1,1]]

for _ in range(N):
    arr = []
    d = dp[-1]
    arr.append(d[1])
    for j in range(1, 9):
        arr.append(d[j-1]+d[j+1])
    arr.append(d[8])
    dp.append(arr)
    
print(sum(dp[N-1])%10**9)