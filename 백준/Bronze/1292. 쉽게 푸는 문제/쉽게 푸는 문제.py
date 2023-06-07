A, B = map(int,input().split())
a = []
n = 0
while len(a) < B:
    n += 1
    a.extend([n for _ in range(n)])
print(sum(a[A-1:B]))