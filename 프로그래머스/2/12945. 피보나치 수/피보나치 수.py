def solution(n):
    ans = []
    for i in range(n+1):
        if i == 0 or i == 1:
            ans.append(i)
        else:
            ans.append((ans[i-1] + ans[i-2]) % 1234567)
    return ans[n]