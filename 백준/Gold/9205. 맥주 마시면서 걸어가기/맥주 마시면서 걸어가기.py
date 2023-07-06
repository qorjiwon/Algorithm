import sys
input = sys.stdin.readline
inf = int(1e9)

for _ in range(int(input())):
    n = int(input())
    location = [list(map(int, input().split())) for _ in range(n+2)]
    graph = [[[inf] for i in range(n+2)] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            distance = abs(location[i][0]-location[j][0])+abs(location[i][1]-location[j][1])
            if distance > 1000:
                graph[i][j]=inf
            else:
                graph[i][j]=1
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])
    if graph[0][n+1] < inf:
        print("happy")
    else:
        print('sad')