from collections import deque

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        arr.append(input().rstrip())
    l = len(arr)
    words = set([arr[i]+arr[j] for i in range(l) for j in range(l) if i != j])
    pallindrome = ''
    for word in words:
        if word[::-1] == word:
            pallindrome = word
            break
    if pallindrome:
        print(pallindrome)
    else:
        print(0)