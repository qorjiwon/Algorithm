from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
nums = counter = Counter(nums)

M = int(input())
targets = list(map(int, input().split()))

print(' '.join([str(nums.get(t, 0)) for t in targets]))