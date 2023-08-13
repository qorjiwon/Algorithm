import sys
input = sys.stdin.readline

N = int(input()) ; k = int(input())

mn = 1
mx = k

while mn <= mx:
    mid = (mn+mx) // 2
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)
    if temp >= k:
        ans = mid
        mx = mid - 1
    else:
        mn = mid + 1
print(ans)