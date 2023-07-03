x = input()
while x != '#':
    print(x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')
          +x.count('A')+x.count('E')+x.count('I')+x.count('O')+x.count('U'))
    x = input()