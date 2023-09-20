str_input = input()
chk = -1
cnt = 0
ans = 0

for idx in range(len(str_input)):
    if str_input[idx] == '(':
        chk = idx
        cnt += 1
    else:
        cnt -= 1
        if chk == (idx - 1):
            ans += cnt

print(ans)