T = int(input())

result = [[] for _ in range(T)]
n=[]
for _ in range(T):
    n.append(int(input()))

for i in range(T):
    j=0
    N = 1
    while n[i] >= N:
        if n[i] & N != 0:
            result[i].append(j)
        j += 1
        N = N << 1
         
for a in result:
    for i in range(len(a)):
        print(a[i], end=' ')
    print()