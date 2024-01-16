def solution(s):
    arr = list(map(int, s.split(' ')))
    answer = ''
    answer = answer + str(min(arr)) + ' ' + str(max(arr))
    return answer