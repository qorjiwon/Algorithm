def solution(n):
    x = list(str(n))
    print(x)
    answer = [int(x[len(x)-i-1]) for i in range(len(x))]
    return answer