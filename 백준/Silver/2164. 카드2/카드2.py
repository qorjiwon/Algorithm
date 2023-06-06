from collections import deque

N = int(input())

queue = deque()
for i in range(N):
    queue.append(i+1)
    
result = queue.popleft()
while queue:
    queue.rotate(-1)
    result = queue.popleft()
    
print(result)
    