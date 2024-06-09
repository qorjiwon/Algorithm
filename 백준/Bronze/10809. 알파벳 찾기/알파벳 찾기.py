str = input()
for alpha in range(ord('a'), ord('z')+1):
    print(str.find(chr(alpha)), end=' ')