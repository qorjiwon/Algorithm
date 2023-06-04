from sys import stdin
input = stdin.readline

result = [0]

for i in range(10):
    a, b = map(int,input().split())
    result.append(result[i]-a+b)
    
print(max(result))