import math

n = int(input())
ans = 0
a = n // 2

for i in range(1, a+1):
    x = i
    y = n - (2 * i)
    anss = math.comb(x + y, min(x, y)) * 2**x
    ans += anss

print((ans+1)%10007)