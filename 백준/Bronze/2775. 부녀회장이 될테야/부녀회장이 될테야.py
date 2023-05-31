T = int(input())

result = []

for _ in range(T):
    k = int(input())
    n = int(input())
    if k == 0:
        result.append(n)
    else:
        r = [i for i in range(1, n+1)]
        for i in range(k):
            new_r = []
            sum = 0
            for j in range(n):
                sum += r[j]
                new_r.append(sum)
            r = new_r
        result.append(r[n-1])
            
for elem in result:
    print(elem)
            
