import sys
input = sys.stdin.readline

N = int(input())
arr = [int((input())) for _ in range(N)]

if N == 1:
    for _ in range(3):
        print(arr[0])
    print(0)
else:
    print(round(sum(arr)/N)) # 산술평균
    arr.sort()
    print(arr[N//2]) # 중앙값
    cnt={} # 빈도 수 구하기
    for i in arr:
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1
    mxcnt = max(cnt.values())
    mx = [e for e in cnt if cnt[e] == mxcnt]
    mx.sort()
    if len(mx) == 1: # 최빈값이 하나일 때
        print(mx.pop())
    else: # 최빈값이 여러 개일 때
        print(mx[1])
    print(arr[N-1]-arr[0]) # 범위