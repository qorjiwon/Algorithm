import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort()
    ans = 1
    minn = arr[0][1]
    for a, b in arr:
        if b < minn:
            minn = b
            ans += 1
    print(ans)