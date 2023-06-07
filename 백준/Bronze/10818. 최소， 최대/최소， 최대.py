import sys

sys.stdin.readline()
a = [int(e) for e in sys.stdin.readline().split()]
print(min(a), max(a))