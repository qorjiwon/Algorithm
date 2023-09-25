n = int(input())
Pebbles = map(int, input().split())
weights = [100, 50, 20, 10, 5, 2, 1]
s = [0,0]

for p in Pebbles:
    if s[0] <= s[1]:
        s[0] += p
    else:
        s[1] += p

a = abs(s[0]-s[1])
ans = 0

while a:
    for w in weights:
        ans += a//w
        a %= w
print(ans)