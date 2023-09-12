import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [0]*n
ans[0]=arr[0]
for i in range(1,n):
    if ans[i-1] <= 0:
        ans[i] = arr[i]
    else:
        ans[i] = ans[i-1]+arr[i]
print(max(ans))