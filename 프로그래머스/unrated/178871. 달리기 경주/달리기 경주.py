def solution(players, callings):
    arr = {}
    ar = {}
    for i in range(len(players)):
        arr[i] = players[i]
        ar[players[i]] = i
        
    for call in callings:
        idx = ar[call]
        temp = arr[idx-1]
        arr[idx-1] = arr[idx]
        arr[idx] = temp
        ar[arr[idx]] = idx
        ar[arr[idx-1]] = idx-1
           
    players = [arr[i] for i in range(len(players))]
    return players