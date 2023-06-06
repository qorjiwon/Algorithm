import heapq, sys

heap = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    elif n > 0 :
        heapq.heappush(heap, (n,n))
    else:
        heapq.heappush(heap, (-n,n))