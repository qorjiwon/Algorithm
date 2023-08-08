import sys
input = sys.stdin.readline

N = int(input())

for i in range(1,N):
    n = list(map(int, list(str(i))))
    if i+sum(n) == N:
        print(i)
        exit()
print(0)