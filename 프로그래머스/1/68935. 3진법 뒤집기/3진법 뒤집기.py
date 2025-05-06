import math
def solution(n):
    if n == 0: return ans
    nums = []
    while n:
        n, digit = divmod(n,3)
        print('n: ', n, ' | digit:', digit)
        nums.append(str(digit))
    ans = 0
    print(''.join(nums))
    for idx, e in enumerate(reversed(nums)): # num 자체가 이미 3진수 거꾸로 되어있음.
        ans += int(e)*math.pow(3, idx)
    return ans