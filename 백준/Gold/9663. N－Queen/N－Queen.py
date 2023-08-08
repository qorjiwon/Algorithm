import sys
input = sys.stdin.readline

N = int(input())
col = [-1]*(N+1)
result = 0

def queens(i):
    global result
    if promising(i): # 유망하면
        if i == N:
            result += 1
        else:
            for j in range(N):
                col[i+1] = j
                queens(i+1)
                
def promising(i):
    k = 1
    while k < i:
        if col[i]==col[k] or abs(col[i]-col[k]) == i-k:
            # i번째 행과 k번째 행에서의 queen의 위치가 같은 열이거나
            # 대각선 방향에 있으면
            return 0 # 유망하지 않음
        k += 1
    return 1 # 유망함

queens(0)
print(result)