import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
min_dist = 1 # 최소 간격
max_dist = house[-1]-house[0] # 최대 간격
while min_dist <= max_dist:
    cnt = 1
    mid = (min_dist+max_dist)//2
    last_install = 0
    for i in range(1,len(house)):
        if house[last_install]+mid <= house[i]:
            cnt += 1
            last_install = i
    if C <= cnt: # 충분히 설치함. 거리를 늘려보자.
        min_dist = mid+1
    elif C > cnt: # 설치 부족. 거리 줄여.
        max_dist = mid-1
print(max_dist)