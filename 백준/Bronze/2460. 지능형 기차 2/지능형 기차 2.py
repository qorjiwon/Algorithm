from sys import stdin
input = stdin.readline

max = 0
num = 0

for i in range(10):
    a, b = map(int,input().split())
    num = num-a+b
    if max < num:
        max = num
    
print(max)