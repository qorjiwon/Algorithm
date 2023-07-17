def solution(players, callings):
    arr = {}
    ar = {}
    for i, player in enumerate(players):
        arr[i] = player
        ar[player] = i
        
    for call in callings:
        idx = ar[call]
        temp = arr[idx-1]
        arr[idx-1] = arr[idx]
        arr[idx] = temp
        ar[arr[idx]] = idx
        ar[arr[idx-1]] = idx-1
           
    players = [arr[i] for i in range(len(players))]
    return players