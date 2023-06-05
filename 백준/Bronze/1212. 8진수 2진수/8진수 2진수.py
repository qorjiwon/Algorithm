from sys import stdin
input = stdin.readline

x = input()
result = bin(int(x, 8))
print(result[2:])