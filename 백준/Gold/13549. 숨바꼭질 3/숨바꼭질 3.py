N, K = map(int, input().split())
visit = [-1]*100001
visit[N]=0

if N > K:
    print(N-K)
else:
    from collections import deque
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            print(visit[x])
            break
        if x < 50001 and visit[x*2] == -1:
            visit[x*2] = visit[x]
            q.appendleft(x*2)
        if 0 < x and visit[x-1] == -1:
            visit[x-1] = visit[x]+1
            q.append(x-1)
        if x < 100000 and visit[x+1] == -1:
            visit[x+1] = visit[x]+1
            q.append(x+1)