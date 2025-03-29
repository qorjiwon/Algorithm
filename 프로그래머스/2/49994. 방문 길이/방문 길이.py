def solution(dirs):
    horizontal = [[0]*10 for _ in range(11)]
    vertical = [[0]*11 for _ in range(10)]
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    x, y = 5, 5
    for dir in dirs:
        dx, dy = directions[dir]
        if (dir == 'U' or dir == 'D'):
            nx = x + dx
            if (-1 < nx < 11):
                vertical[min(x, nx)][y] = 1 # record
                x = nx #move
        else:
            ny = y + dy
            if (-1 < ny < 11):
                horizontal[x][min(y, ny)] = 1 #record
                y = ny # move
            
    answer = sum([sum(v) for v in vertical]) + sum([sum(h) for h in horizontal])
    return answer