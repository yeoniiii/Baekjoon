def solution(s):
    arr = s.split(' ')
    new = []
    for a in arr:
        a_new = ''
        for i in range(len(a)):
            if i == 0 or i % 2 == 0:
                a_new += a[i].upper()
            else:
                a_new += a[i].lower()
        new.append(a_new)
        answer = ' '.join(new)
    return answer