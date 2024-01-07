def solution(num):
    answer = 0
    if num == 1:
        pass
    else:
        while True:
            if num == 1:
                break
            if answer >= 500:
                answer = -1
                break
            elif num % 2 == 0:
                num /= 2
                answer += 1
            else:
                num = num * 3 + 1
                answer += 1
    return answer