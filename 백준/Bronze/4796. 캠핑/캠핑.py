import sys
input = sys.stdin.readline

i = 1
while 1:
    L, P, V = map(int, input().split())
    if not L:
        break
    ans = (V//P)*L + min(V%P, L)
    print(f"Case {i}: {ans}")
    i += 1