n, m = map(int, input().split())
A = []
result = 0

for i in range(n):
    A.insert(0, int(input()))
    
for i in A:
    if (m//i != 0):
        result += m//i
        m = m%i
             
print(result)