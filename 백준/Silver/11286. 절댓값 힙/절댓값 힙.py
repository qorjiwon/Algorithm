import heapq, sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    elif n > 0 :
        heapq.heappush(heap, (n,n))
    else:
        heapq.heappush(heap, (-n,n))