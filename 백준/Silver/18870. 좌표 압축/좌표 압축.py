import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
s = set(nums)
s = list(s)
s.sort()
d = {}
for i in range(len(s)):
    d[s[i]]=i
for n in nums:
    print(d[n], end = ' ')