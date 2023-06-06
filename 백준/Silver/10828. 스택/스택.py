from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
for _ in range(int(input())):
    s = input().split()
    if len(s) == 2:
        if s[0] == 'push':
            queue.append(s[1])
    else:
        s = s[0]
        if s == 'pop':
            if queue:
                print(queue.pop())
            else:
                print(-1)
        elif s=='size':
            print(len(queue))
        elif s=='empty':
            if queue:
                print(0)
            else:
                print(1)
        else:
            if queue:
                n = queue.pop()
                print(n)
                queue.append(n)
            else:
                print(-1)