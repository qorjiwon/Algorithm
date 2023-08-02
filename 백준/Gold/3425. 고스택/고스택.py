import sys
input = sys.stdin.readline

commands = [input().rstrip()]
while commands[0] != 'QUIT':
    if commands[0] != 'END':
        while 1:
            o = input().rstrip()
            if o == 'END':
                break
            else:
                commands.append(o)
            
    s = []
    for _ in range(int(input())):
        s.append(int(input()))
        e = 0 # 에러가 났는지 (0: 에러가 없음, 1: 에러 발생)
        for V in commands:
            try:
                if len(V) == 3:
                    if V == 'POP':
                        s.pop()
                    elif V == 'INV':
                        s[-1]=-s[-1]
                    elif V == 'DUP':
                        s.append(s[-1])
                    elif V == 'SWP':
                        s[-1], s[-2] = s[-2], s[-1]
                    elif V == 'ADD':
                        n = s.pop()+s.pop()
                        if abs(n) > 10**9:
                            e = 1
                            break
                        else:
                            s.append(n)
                    elif V == 'SUB':
                        n = -s.pop()+s.pop()
                        if abs(n) > 10**9:
                            e = 1
                            break
                        else:
                            s.append(n)
                    elif V == 'MUL':
                        n = s.pop()*s.pop()
                        if abs(n) > 10**9:
                            e = 1
                            break
                        else:
                            s.append(n)
                    elif V == 'DIV':
                        v1, v2 = s.pop(), s.pop()
                        if v1 == 0:
                            e = 1
                            break
                        if v1*v2 < 0:
                            s.append(-(abs(v2)//abs(v1)))
                        else:
                            s.append(v2//v1)
                    elif V == 'MOD':
                        v1, v2 = s.pop(), s.pop()
                        if v1 == 0:
                            e = 1
                            break
                        if v1*v2 < 0:
                            t = abs(v2)%abs(v1)
                            if v2 < 0:
                                s.append(-t)
                            else:
                                s.append(t)
                        else:
                            s.append(v2%v1)
                else:
                    if len(V[4:]) <= 10:
                        s.append(int(V[4:]))
                    else:
                        e = 1
                        break
            except:
                e = 1
                break
        if e or len(s) != 1:
            print('ERROR')
        else:
            print(s.pop())
    print()
    input() # 두 번째 입력부터 첫 번째 줄에 공백을 받아옴
    commands = [input().rstrip()]