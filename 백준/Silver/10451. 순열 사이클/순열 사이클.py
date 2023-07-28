import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    visited=[0]*(N+1)
    for i in range(1,N+1):
        if visited[i] == 0:
            visited[i]=1
            go = arr[i-1]
            while go != i:
                visited[go]=1
                go = arr[go-1]
            result += 1
    print(result)