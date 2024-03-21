def solution(s, n):
    print(ord('z'), ord('a')-ord('b'), chr(ord('a')),chr(ord('a')+1), (ord('z')+1)%ord('a'))
    answer = ''.join([' ' if i == ' ' else ( chr( (ord(i)+n-ord('A'))%26+ord('A') ) if i < 'a' else chr( (ord(i)+n-ord('a'))%26+ord('a') ) ) for i in list(s)])
    return answer