import sys
input = sys.stdin.readline

for _ in range(int(input())):
    str = input().rstrip()
    ans = 0
    score = 1
    for x in str:
        if x == 'O':
            ans += score
            score += 1
        else:
            score = 1
    print(ans)