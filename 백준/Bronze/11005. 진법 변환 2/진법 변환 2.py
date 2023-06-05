N, B = map(int, input().split())

n = 0
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while pow(B,n+1) <= N:
    n += 1
    
result=''

while n > -1:
    r = N//pow(B,n)
    N = N%pow(B,n)
    if r > 9:
        r -= 10
        result += a[r]
    else:
        result += str(r)
    n -= 1

print(result)