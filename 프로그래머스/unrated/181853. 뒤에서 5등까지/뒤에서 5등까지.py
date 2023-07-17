def solution(num_list):
    answer = []
    for _ in range(5):
        m = min(num_list)
        answer.append(m)
        num_list.remove(m)
    return answer