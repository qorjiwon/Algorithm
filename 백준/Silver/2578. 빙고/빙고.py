import sys
input = sys.stdin.readline

m1 = []
m2 = []

for _ in range(5):
    m1.append(list(map(int, input().split())))
for _ in range(5):
    m2.append(list(map(int, input().split())))

def bingo(m):
    num = 0
    # check rows
    for i in range(5):
        if m[i][0] == 0 and m[i][1] == 0 and m[i][2] == 0 and m[i][3] == 0 and m[i][4] == 0:
            num += 1
    # check columns
    for i in range(5):
        if m[0][i] == 0 and m[1][i] == 0 and m[2][i] == 0 and m[3][i] == 0 and m[4][i] == 0:
            num += 1
    # check diagonals
    if m[0][0] == 0 and m[1][1] == 0 and m[2][2] == 0 and m[3][3] == 0 and m[4][4] == 0:
        num += 1
    if m[4][0] == 0 and m[3][1] == 0 and m[2][2] == 0 and m[1][3] == 0 and m[0][4] == 0:
        num += 1
    return num

ans = 0
for low in m2:
    for e in low:
        ans += 1
        for i in range(5):
            for j in range(5):
                if m1[i][j] == e:
                    m1[i][j] = 0
        if bingo(m1) >= 3:
            print(ans)
            sys.exit(0)