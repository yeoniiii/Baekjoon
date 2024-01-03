def solution(n):
    arr = list(map(int, str(n)))
    arr.sort(reverse=True)
    answer = ''
    for i in arr:
        answer += str(i)
    return int(answer)