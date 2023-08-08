import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int,input().split()))
max_high = max(tree)
min_high = 0
high = max_high//2

while min_high <= max_high:
    high = (min_high+max_high)//2
    s = 0
    for t in tree:
        if high < t:
            s += t-high
    if s < M: # 설정 높이가 너무 높을 때
        max_high = high-1
    elif s >= M: # 설정 높이가 너무 낮을 때
        min_high = high+1
        
print(max_high)