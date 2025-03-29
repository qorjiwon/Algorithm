def solution(N, stages):
    cnt_user = [0]*(N+2) # 각 스테이지별 클리어한 사용자 수 배열
    for stage in stages:
        for i in range(1, stage+1):
            cnt_user[i] += 1
    rates = [[i, stages.count(i)/cnt_user[i] if cnt_user[i] != 0 else 0] for i in range(1, N+1)]
    rates = sorted(rates, key=lambda x:x[1], reverse=True)
    answer = [rate[0] for rate in rates]
    return answer