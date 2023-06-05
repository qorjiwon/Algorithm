import sys
input = sys.stdin.readline

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
    
for _ in range(int(input())):
    result = 0
    arr = list(map(int, input().split()))
    n = arr[0]
    for a in range(1,n):
        for b in range(a+1,n+1):
            result += gcd(arr[a],arr[b])
    print(result)