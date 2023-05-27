result=0
n = input()
m = input()
idx = 0
while (n.find(m, idx) != -1):
    idx = n.find(m, idx) + len(m)
    result += 1

print(result)