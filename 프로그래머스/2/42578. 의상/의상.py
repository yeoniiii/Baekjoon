def solution(clothes):
    d = {}
    for cloth in clothes:
        if cloth[1] in d:
            d[cloth[1]] += 1
        else:
            d[cloth[1]] = 1
    answer = 1
    for val in d.values():
        answer *= (val+1)
    return answer - 1