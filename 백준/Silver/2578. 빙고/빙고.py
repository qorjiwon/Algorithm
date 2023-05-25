chulsu = []
for i in range(5):
    chulsu.append(list(map(int, input().split())))
    
dae=[[],[]]
for i in range(5):
    dae[0].append(chulsu[i][i])
for i in range(5):
    dae[1].append(chulsu[i][4-i])
    
ga=[[],[],[],[],[]]
for i in range(5):
    for j in range(5):
        ga[i].append(chulsu[i][j])

sae =[[],[],[],[],[]]

for i in range(5):
    for j in range(5):
        sae[i].append(chulsu[j][i])


sa = []
for i in range(5):
    sa.append(list(map(int, input().split())))
    
result = 1
for i in range(5):
    gameover = 0
    for j in range(5):
        bingo = 0
        
        for k in range(2):
            for r in range(len(dae[k])):
                if (sa[i][j]==dae[k][r]):
                    dae[k].pop(r)
                    break
                    
        for k in range(5):
            for r in range(len(ga[k])):
                if(sa[i][j] == ga[k][r]):
                    ga[k].pop(r)
                    break
            for r in range(len(sae[k])):
                if(sa[i][j] == sae[k][r]):
                    sae[k].pop(r)
                    break
            
        for k in range(2):
            if(len(dae[k])==0):
                bingo += 1
        for k in range(5):
            if (len(ga[k])==0):
                bingo += 1
            if (len(sae[k])==0):
                bingo += 1
            
        if (bingo >2):
            gameover = 1
            break
        else:
            result += 1
        
    if (gameover):
        break
            

print(result)