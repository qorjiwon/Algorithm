import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
checkout_cards = list(map(int, input().split()))

def cnt(arr, target):
    left, right = 0, len(arr) - 1
    first, last = -1, -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
            if arr[mid] == target:
                first = mid
        else:
            left = mid + 1

    if first == -1:
        return 0

    left, right = 0, len(arr) - 1

    # Find last occurrence
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
            if arr[mid] == target:
                last = mid
        else:
            right = mid - 1

    return last - first + 1

ans = []
for card in checkout_cards:
    ans.append(str(cnt(cards, card)))

print(' '.join(ans))