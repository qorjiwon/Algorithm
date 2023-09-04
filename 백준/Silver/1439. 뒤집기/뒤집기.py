s = [int(e) for e in list(input())]

ans = [0,0] # [이어진 0 개수, 이어진 1 개수]
n = s[0] # 첫 번째 숫자
ans[n] = 1 # 이어진 첫 번째 숫자의 개수를 1로

for e in s:
    if n != e:
        n = e
        ans[n] += 1
print(min(ans))