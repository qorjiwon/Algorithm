import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    arr = [0]*max(n+1,4)
    arr[1]=1
    arr[2]=2
    arr[3]=4
    for i in range(4,n+1):
        arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    print(arr[n])