from collections import Counter 
a = input().upper()
if len(a) == 1:
    print(a.upper())
else:
    v = Counter(a).most_common()
    if v[0][1] == v[1][1]:
        print('?')
    else:
        print(v[0][0])