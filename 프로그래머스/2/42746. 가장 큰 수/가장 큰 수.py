def solution(numbers):
    answer = ''
    
    numbers.sort(reverse=True,
                 key = lambda x: str(x)*3)
    for n in numbers:
        answer += str(n)
    return str(int(answer))