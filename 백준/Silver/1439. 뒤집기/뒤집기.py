s = list(input())

ans = 1 # 같은 숫자끼리 연속된 영역 개수
for i in range(len(s)-1):
    if s[i] != s[i-1]:
        ans += 1
print(ans//2) # 영역 3개 -> 1번 뒤집기, 영역 4개 -> 2번 뒤집기