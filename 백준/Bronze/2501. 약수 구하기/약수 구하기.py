N, K = map(int, input().split())

a = 0
result = 0
for i in range(1, N+1):
    if N % i == 0:
        a += 1
        result = i
    if a == K:
        break
if a == K:
    print(result)
else:
    print(0)