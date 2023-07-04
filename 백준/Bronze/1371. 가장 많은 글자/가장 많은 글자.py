c = [[0,x] for x in range(97,123)]
try:
    while 1:
        s=input()
        for i in range(len(s)):
            for j in range(len(c)):
                if s[i] == ' ':
                    break
                elif s[i] == chr(c[j][1]):
                    c[j][0] += 1
                    break
except:
    c.sort(reverse=1)
    result = []
    result.append(chr(c[0][1]))
    for i in range(1,len(c)):
        if c[i][0] == c[0][0]:
            result.append(chr(c[i][1]))
        
    result.sort()
    print(''.join(result))
                
