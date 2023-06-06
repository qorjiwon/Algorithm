import heapq, sys
input = sys.stdin.readline

heap = []
_heap = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(heap) and len(_heap):
            a = heapq.heappop(heap)
            b = heapq.heappop(_heap)
            if a < b:
                print(a)
                heapq.heappush(_heap, b)
            else:
                print(-b)
                heapq.heappush(heap, a)
        elif len(heap):
            print(heapq.heappop(heap))
        elif len(_heap):
            print(-heapq.heappop(_heap))
        else:
            print(0)
    elif n > 0 :
        heapq.heappush(heap, n)
    else:
        heapq.heappush(_heap, -n)