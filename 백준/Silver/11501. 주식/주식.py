T = int(input())
for i in range(T):
    A = []
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    m = 0
    for i in range(N-1, -1, -1):
        if (m < A[i]):
            m = A[i]
        result += m - A[i]
    print(result)