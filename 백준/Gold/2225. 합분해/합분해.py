def fac(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

N, K = map(int, input().split())
print(fac(N+K-1)//(fac(N)*fac(K-1))%1000000000)