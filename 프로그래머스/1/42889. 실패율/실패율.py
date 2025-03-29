def solution(N, stages):
    stages.sort()
    cnt_user = [len(stages)]*(N+2) # 각 스테이지별 도달한 사용자 수 배열
    notyet = 0 # 아직 도달 못한 사용자 수
    
    for i in range(1, N+1):
        cnt_user[i] -= notyet
        notyet += stages.count(i)
        
    rates = [[i, stages.count(i)/cnt_user[i] if cnt_user[i] != 0 else 0] for i in range(1, N+1)]
    rates = sorted(rates, key=lambda x:x[1], reverse=True)
    answer = [rate[0] for rate in rates]
    return answer