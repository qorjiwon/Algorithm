N = int(input())

game=[]
d=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    game.append(list(map(int, input().split())))

d[0][0]=1
for y in range(N):
    for x in range(N):
        # print('x= ', x, 'y= ', y)
        if x+game[y][x]<N:
            d[y][x+game[y][x]] += d[y][x]
            # print(x+game[y][x], y, "+", d[y][x])
        if y+game[y][x]<N:
            d[y+game[y][x]][x] += d[y][x]
            # print(x, y+game[y][x], '+', d[y][x])
#위에 이중 for문에서 y=x=N-1일 때 x2, x2 되는 경우 때문에 나누어줌
d[N-1][N-1] //= 4
# print('game\n', game)
# print('d\n', d)
# print('result\n', d[N-1][N-1])

print(d[N-1][N-1])