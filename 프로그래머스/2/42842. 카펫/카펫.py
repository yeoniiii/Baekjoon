def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            j = yellow // i
            if (i+2) * (j+2) == (brown+yellow):
                answer = [j+2, i+2]
                return answer