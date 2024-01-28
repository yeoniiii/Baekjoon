def solution(s):
    arr = list(s.split(" "))
    ans = []
    for a in arr:
        if a == '': # 공백
            pass
        elif a.isdigit() == False: # 문자
            a = a[0].upper() + a[1:].lower()
        ans.append(a)
    answer = ' '.join(ans, )
    return answer