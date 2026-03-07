def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    real_lost = [l for l in lost]
    
    for l in lost: # 못빌려주는 학생 제거
        if l in reserve:
            reserve.remove(l)
            real_lost.remove(l)
    ans = n-len(real_lost)
    
    for l in real_lost: # 체육복 빌려주기
        if l-1 in reserve:
            ans += 1
        elif l+1 in reserve:
            ans += 1
            reserve.remove(l+1)
            
    return ans