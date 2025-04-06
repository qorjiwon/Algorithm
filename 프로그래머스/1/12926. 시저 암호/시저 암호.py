def solution(s, n):
    # ord('a')=97, ord('z')=122
    # ord('A')=65, ord('Z')=90
    n = n%26
    return  ''.join(
        [ ch if ch == ' ' 
         else (
             ( chr(96 + ord(ch)+n-122) if ord(ch)+n > 122 else chr(ord(ch)+n) ) if ord(ch) > 90 # 소문자
             else ( chr(64 + ord(ch)+n-90) if ord(ch)+n > 90 else chr(ord(ch)+n) ) # 대문자
         )
         for ch in s
        ])