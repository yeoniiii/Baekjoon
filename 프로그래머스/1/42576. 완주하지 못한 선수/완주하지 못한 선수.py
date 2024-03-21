def solution(participant, completion):
    answer = ''
    part = dict()
    for p in participant:
        if p in part:
            part[p] += 1
        else:
            part[p] = 1
    for c in completion:
        part[c] -= 1
    for k, v in part.items():
        if v == 1:
            answer = k
        
    return answer