from collections import deque

import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        arr.append(input().rstrip())
    l = len(arr)
    words = set([arr[i]+arr[j] for i in range(l) for j in range(l) if i != j])
    isP = False
    for word in words:
        if word[::-1] == word:
            isP = True
            break
    if isP:
        ans.append(word)
    else:
        ans.append(0)

for a in ans:
    print(a)