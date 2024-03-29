import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)] # 스티커 점수 배열
    dp = [[e for e in x] for x in s] # 스티커 점수 배열 복사
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for y in range(2, n):
            for x in range(2):
                for xx in range(2):
                    for yy in range(y-2, y):
                        if abs(x-xx)+abs(y-yy) > 1:
                            dp[x][y] = max(dp[x][y], dp[xx][yy]+s[x][y])
        print(max(max(dp[0]), max(dp[1])))