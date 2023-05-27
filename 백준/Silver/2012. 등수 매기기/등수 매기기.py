A = []
from sys import stdin
n = int(stdin.readline())
result = 0
for i in range(n):
    A.append(int(input()))

A.sort()
for i in range(1,n+1):
    result += abs(A[i-1]-i)
    
print(result)