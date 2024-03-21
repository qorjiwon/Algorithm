import re

def solution(s):
    answer = True if (len(s) == 4 or len(s) == 6) and len(re.findall('[^0-9]', s))==0 else False
    return answer