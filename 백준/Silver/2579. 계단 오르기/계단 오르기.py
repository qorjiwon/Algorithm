T = int(input())

d=[0]
s=[0]*(T+1)
for _ in range(T):
    d.append(int(input()))
if T<3:
    for _ in range(T,5):
        d.append(0)
        s.append(0)


s[1]=d[1]
s[2]=d[1]+d[2]
s[3]=d[3]+max(d[1],d[2])
s[4]=d[4]+max(d[1]+d[2], d[1]+d[3])
for i in range(4, T+1):
    s[i]=d[i]+max(d[i-1]+s[i-3], s[i-2])

print(s[T])
# print('result d')
# print(d)
# print('result s')
# print(s)