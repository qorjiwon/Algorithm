N = int(input())
a, b = 0, 1
for i in range(N-1):
    a, b = b, a+b
print(b)