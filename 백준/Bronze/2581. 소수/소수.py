M = int(input())
N = int(input())
a = list(range(M, N+1))
ans = list(range(M, N+1))
if M == 1:
    a.pop(0)
    ans.pop(0)
    
for elem in a:
    for i in range(2, elem//2+1):
        if elem%i == 0:
            ans.remove(elem)
            break
if len(ans):
    print(sum(ans))
    print(ans[0])
else:
    print(-1)