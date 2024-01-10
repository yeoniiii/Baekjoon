def solution(phone_number):
    last = phone_number[-4:]
    first = phone_number[:-4]
    answer = '*'*len(first) + last
    return answer