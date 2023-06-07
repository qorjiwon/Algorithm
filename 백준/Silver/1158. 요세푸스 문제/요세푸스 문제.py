import sys
N, K = map(int,sys.stdin.readline().split())

a = list(range(1,N+1))
ans = []
i = 0
while a:
    i = (i+K-1)%len(a)
    ans.append(a.pop(i))
print('<'+', '.join(map(str,ans))+'>')