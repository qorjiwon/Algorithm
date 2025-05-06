import re

def solution(s):
    return True if re.fullmatch("[0-9]{4}|[0-9]{6}", s) else False