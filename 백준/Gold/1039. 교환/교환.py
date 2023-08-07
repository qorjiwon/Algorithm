import sys
input = sys.stdin.readline

N, K = input().split()
K = int(K)
M = len(N)
N = list(map(int,N))

if M == 1:
    print(-1)
elif M == 2 and N[1]==0:
    print(-1)
else:
    from collections import deque
    q = deque([(0, N)])
    dp = []
    ans = []
    loop = 0
    for e in N:
        if N.count(e)>1: # 같은 글자가 존재하는지
            loop =1
    while q:
        e = q.popleft()
        k, arr = e[0], e[1]
        if k == K:
            ans.append(int("".join(map(str,arr))))
        else:
            num = 1
            for i in range(M-1):
                for j in range(i+1,M):
                    if i or arr[j] != 0:
                        newArr = [e for e in arr]
                        newArr[i], newArr[j] = newArr[j], newArr[i]
                        number = int("".join(map(str,newArr)))
                        if number not in dp:
                            q.append((k+1, newArr))
                            num += 1
                            dp.append(number)
                            if (K-k-1)%2 == 0: # 남은 이동 횟수가 짝수면
                                ans.append(number)
                            elif loop:
                                ans.append(number)
    print(max(ans))