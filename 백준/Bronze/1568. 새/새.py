time = 0
N = int(input())
i=1
while N > 0:
    if N < i:
        i = 1
        continue
    N -= i
    time += 1
    i += 1
print(time)