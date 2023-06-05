import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = 0
    arr = list(map(int, input().split()))
    n = arr[0]
    for a in range(1,n):
        for b in range(a+1,n+1):
            GCD = 1
            if arr[a] < arr[b]:
                GCD = arr[a]
                while arr[a]%GCD + arr[b]%GCD != 0:
                    GCD -= 1
            else:
                GCD = arr[b]
                while arr[a]%GCD + arr[b]%GCD != 0:
                    GCD -= 1
            result += GCD
    print(result)