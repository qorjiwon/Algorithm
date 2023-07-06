time = 0
N = int(input())
i=0
while N > 0:
    i += 1
    if N < i:
        i = 0
        continue
    N -= i
    time += 1
print(time)