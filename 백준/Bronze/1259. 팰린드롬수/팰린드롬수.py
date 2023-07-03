import sys
input = sys.stdin.readline

x = input().rstrip()
while int(x):
    if x == x[::-1]:
        print('yes')
    else:
        print('no')
    x = input().rstrip()