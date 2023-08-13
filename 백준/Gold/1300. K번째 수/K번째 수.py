import sys
input = sys.stdin.readline

N = int(input()) ; k = int(input())
mn, mx = 1, k

while mn <= mx:
    mid = (mn+mx) // 2
    n = 0 # mid값보다 작은 요소 개수
    for i in range(1, N+1):
        n += min(mid//i, N) # i번째 행에서 mid값보다 작은 요소 개수
    if n < k: # k개보다 적으면 더 큰 값 조사
        mn = mid + 1
    else: # k개보다 많거나 같으면 더 작은 값 조사
        mx = mid - 1
print(mn)