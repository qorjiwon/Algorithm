import sys
input = sys.stdin.readline

i = 1
while 1:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    ans = (V//P)*L
    ans += min(V%P, L)
    print('Case ',i,': ',ans,sep='')
    i += 1