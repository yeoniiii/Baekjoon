def solution(s):
    answer = s.isdigit() and len(s) in [4, 6]
    return answer