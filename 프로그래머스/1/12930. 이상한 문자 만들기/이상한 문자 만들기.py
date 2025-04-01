def solution(s):
    ans = []
    idx = 0
    for e in s:
        if e == ' ':
            ans.append(e)
            idx = 0
        else:
            ans.append(e.upper() if idx%2==0 else e.lower())
            idx += 1
    return ''.join(ans)