import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
max_length = max(lan)
min_length = 1
while min_length <= max_length:
    length = (min_length+max_length)//2
    cnt = 0
    for e in lan:
        cnt += e//length
    if cnt < N: # 개수가 모자람 -> 길이를 더 짧게
        max_length = length-1
    else: # cnt >= N 이므로 일단 만족. 개수가 많음 -> 길이를 더 길게
        min_length = length+1
print(max_length)