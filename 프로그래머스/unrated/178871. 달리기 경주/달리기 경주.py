def solution(players, callings):
    arr = {key:i for i, key in enumerate(players)}
        
    for player in callings:
        rank = arr[player]
        arr[player] -= 1
        arr[players[rank-1]] += 1
        players[rank], players[rank-1] = players[rank-1], players[rank]
           
    return players
