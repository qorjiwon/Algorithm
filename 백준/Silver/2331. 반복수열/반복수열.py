A, P = map(int, input().split())
D=[]
D.append(A)
i = 0
while 1:
    D.append(0)
    D[i] = str(D[i])
    for j in range(len(D[i])):
        D[i+1] += pow(int(D[i][j]), P)
    D[i] = int(D[i])
    i += 1
    if D[i] in D[:i]:
        break

# print(D)
print(D.index(D[i]))