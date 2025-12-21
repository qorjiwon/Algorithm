import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
targets = list(map(int, input().split()))

ans = {}
for n in nums:
    if n in ans:
        ans[n] += 1
    else:
        ans[n] = 1

print(' '.join([str(ans.get(t, 0)) for t in targets]))