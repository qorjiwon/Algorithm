import sys
input = sys.stdin.readline

N = int(input())
cost_RGB = [list(map(int,input().split())) for _ in range(N)]
cost = [[0]*3 for _ in range(N)]
cost[0] = cost_RGB[0]
for i in range(1, N):
    cost[i][0] = min(cost[i-1][1],cost[i-1][2])+cost_RGB[i][0]
    cost[i][1] = min(cost[i-1][0],cost[i-1][2])+cost_RGB[i][1]
    cost[i][2] = min(cost[i-1][0],cost[i-1][1])+cost_RGB[i][2]
print(min(cost[N-1]))