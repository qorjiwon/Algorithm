from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
for _ in range(int(input())):
    s = input().split()
    if len(s) == 2:
        if s[0] == 'push_back':
            queue.append(int(s[1]))
        elif s[0] == 'push_front':
            queue.appendleft(int(s[1]))
    else:
        s = s[0]
        if s == 'pop_back':
            if queue:
                print(queue.pop())
            else:
                print(-1)
        elif s == 'pop_front':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif s == 'size':
            print(len(queue))
        elif s == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif s == 'front':
            if queue:
                tmp = queue.popleft()
                print(tmp)
                queue.appendleft(tmp)
            else:
                print(-1)
        elif s == 'back':
            if queue:
                tmp = queue.pop()
                print(tmp)
                queue.append(tmp)
            else:
                print(-1)