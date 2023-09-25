n = int(input())
height = list(map(int, input().split()))
avg = sum(height)//n
ans1, ans2 = 0, 0
for h in height:
    if h > avg:
        ans1 += h-avg-1
    else:
        ans2 += avg-h
print(max(ans1, ans2))