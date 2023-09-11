import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    ans = [0]*n
    ans[0] = arr[0]
    ans[1] = arr[0]+arr[1]
    ans[2] = max(ans[0],arr[1])+arr[2]
    for i in range(3,n):
        ans[i] = max(ans[i-2],ans[i-3]+arr[i-1])+arr[i]
    print(ans[n-1])