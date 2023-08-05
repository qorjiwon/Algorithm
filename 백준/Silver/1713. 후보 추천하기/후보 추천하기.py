import sys
input = sys.stdin.readline

N = int(input())
R = int(input())
arr = list(map(int,input().rstrip().split()))
rec = []

def find_idx(e):
    idx = -1
    for k in range(len(rec)):
        if rec[k][2] == e:
            idx = k
            break
    return idx

for i in range(R):
    if len(rec) == N: # 비어있는 사진틀이 없는 경우
        idx = find_idx(arr[i])
        if idx == -1:
            rec.sort(reverse=True)
            rec.pop()
            rec.append([1,i,arr[i]])
        else:
            rec[idx][0] += 1
    else:
        idx = find_idx(arr[i])
        if idx == -1:
            rec.append([1,i,arr[i]]) # R-i가 작을수록(i가 클수록) 최근 사진
        else:
            rec[idx][0] += 1
        
rec.sort(reverse=True)
result = [e[2] for e in rec]
result.sort()
print(*result)