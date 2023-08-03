import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
nc = ['a','c','i','n','t']

def f(learned, n):
    if n == len(aa):
        if len(learned) == K:
            ans = 0
            for word in words:
                okay = 1
                for s in word:
                    if s not in learned:
                        okay = 0
                        break
                if okay:
                    ans += 1
            return ans
        return 0
    else:
        return max(f(learned+[aa[n]], n+1), f(learned, n+1))
    
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    a =[chr(x) for x in range(97,123) if chr(x) not in nc] # 알파벳 종류
    c = [0 for _ in range(21)] # 빈도 수

    for i in range(21):
        for word in words:
            c[i] += word.count(a[i])

    aa = [a[i] for i in range(21) if 0 < c[i]] # 단어에 있는 알파벳만
    learned = []
    if K < len(aa)+5:
        print(f(nc, 0))
    else:
        print(N)