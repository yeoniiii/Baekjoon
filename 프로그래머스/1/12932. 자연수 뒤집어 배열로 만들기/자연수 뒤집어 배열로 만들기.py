def solution(n):
    answer = []
    n = str(n)
    l = len(n)
    for i in range(l):
        answer.append(int(n[l-i-1]))
    return answer