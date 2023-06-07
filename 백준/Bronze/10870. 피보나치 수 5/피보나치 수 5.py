n = int(input())

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a = [0, 1]
    for i in range(1, n):
        a.append(a[i]+a[i-1])
    print(a[n])