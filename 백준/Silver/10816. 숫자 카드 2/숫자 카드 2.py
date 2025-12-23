from collections import Counter

N = int(input())
nums = Counter(list(map(int, input().split())))

M = int(input())
targets = list(map(int, input().split()))

print(' '.join([str(nums.get(t, 0)) for t in targets]))