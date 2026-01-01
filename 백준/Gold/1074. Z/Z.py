N, R, C = map(int, input().split())

x, y = 0, 0
a, b, c, d = 0, 2**N-1, 0, 2**N-1
ans = 0

while N > 0:
    x = (a+b)//2
    y = (c+d)//2
    
    if R <= x and C <= y:
        b = x
        d = y
    elif R <= x and C > y:
        b = x
        c = y+1
        ans += 2**(2*N-2)
    elif R > x and C <= y:
        a = x+1
        d = y
        ans += 2*(2**(2*N-2))
    else:
        a = x+1
        c = y+1
        ans += 3*(2**(2*N-2))
    N -= 1

print(ans)