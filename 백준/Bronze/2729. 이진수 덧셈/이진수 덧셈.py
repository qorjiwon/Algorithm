import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    a_ = 0
    b_ = 0
    for i in range(len(a)):
        a_ += int(a[len(a)-i-1])*pow(2, i)
    for i in range(len(b)):
        b_ += int(b[len(b)-i-1])*pow(2, i)
    print(bin(a_+b_)[2:])