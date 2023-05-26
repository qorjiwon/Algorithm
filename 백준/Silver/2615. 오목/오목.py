ba=[list(map(int, input().split())) for _ in range(19)]

winner = 0
end = 0
z = []

for x in range(19):
    for y in range(19):
        #print('x: ', x, 'y: ', y)
        if ba[y][x]:
            winner = ba[y][x]
            #print("predict winner: ", winner)
            if y < 15:
                if not end:
                    #print('case1')
                    for i in range(1,5):
                        end=1
                        if ba[y+i][x] != winner:
                            end=0
                            break
                    if end:
                        if y<14:
                            if ba[y+5][x] == winner:
                                end = 0
                        if y>0:
                            if ba[y-1][x] == winner:
                                end = 0
                if x < 15 and not end:
                    #print('case2')
                    end=1
                    for i in range(1, 5):
                        if ba[y+i][x+i] != winner:
                            end=0
                            break
                    if end:
                        if y<14 and x<14:
                            if ba[y+5][x+5] == winner:
                                end = 0
                        if y>0 and x>0:
                            if ba[y-1][x-1] == winner:
                                end = 0
            if x < 15 and not end:
                #print('case3')
                end=1
                for i in range(1, 5):
                    if ba[y][x+i] != winner:
                        end = 0
                        break
                if end:
                    if x<14:
                        if ba[y][x+5] == winner:
                            end = 0
                    if x>0:
                        if ba[y][x-1] == winner:
                            end = 0
                if not end and y>3:
                    #print('case4')
                    end=1
                    for i in range(1, 5):
                        if ba[y-i][x+i] != winner:
                            end = 0
                    if end:
                        if y>4 and x<14:
                            if ba[y-5][x+5] == winner:
                                end = 0
                        if y<18 and x>0:
                            if ba[y+1][x-1] == winner:
                                end = 0
        if end:
            z.append(y+1)
            z.append(x+1)
            break
    if end:
        break

if end:
    print(winner)
    print(z[0], z[1])
else:
    print(0)