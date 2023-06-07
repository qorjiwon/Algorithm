import sys
N, K = map(int,sys.stdin.readline().split())

a = [i for i in range(1,N+1)]
ans = []
i = 0

while a:
    i = (i+K-1)%len(a)
    ans.append(str(a[i]))
    a.remove(a[i])

print('<'+', '.join(ans)+'>')