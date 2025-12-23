import sys
input = sys.stdin.readline

d = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 왼 위 오 아

for _ in range(int(input())):
    x, y = 0, 0
    direction = 1
    left, right, top, bottom = 0, 0, 0, 0
    order = input().strip()
    for step in order:
        if step == 'F':
            x += d[direction][0]
            y += d[direction][1]
        elif step == 'B':
            x -= d[direction][0]
            y -= d[direction][1]
        elif step == 'L':
            direction = (direction - 1) % 4
        elif step == 'R':
            direction = (direction + 1) % 4
        left = min(left, x)
        right = max(right, x)
        bottom = min(bottom, y)
        top = max(top, y)
    print((right - left) * (top - bottom))