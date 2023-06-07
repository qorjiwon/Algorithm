import sys
input = sys.stdin.readline
N = int(input())
a=list(map(int, input().split()))
ans = len(a)
for i in range(N):
    if a[i] == 1:
        ans -= 1
    else:
        for j in range(2,a[i]//2+1):
            if a[i]%j == 0:
                ans -= 1
                break
print(ans)