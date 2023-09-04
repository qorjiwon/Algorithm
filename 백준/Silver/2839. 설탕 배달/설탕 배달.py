N = int(input())
for i in range(N//5+1):
    if (N%5+5*i)%3 == 0:
        ans = N//5-i
        ans += (N%5+5*i)//3
        print(ans)
        exit()
print(-1)