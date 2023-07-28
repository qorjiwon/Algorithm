import sys
input = sys.stdin.readline

def dfs(arr,idx,k,lotto):
    if len(lotto) == 6:
        print(*lotto)
    else:
        for i in range(idx+1,k):
            l = [e for e in lotto]
            l.append(arr[i])
            dfs(arr,i,k,l)
    
k, *arr = map(int, input().split())
while k:
    arr.sort()
    for i in range(k-5):
        dfs(arr,i,k,[arr[i]])
    k, *arr = map(int, input().split())
    print()