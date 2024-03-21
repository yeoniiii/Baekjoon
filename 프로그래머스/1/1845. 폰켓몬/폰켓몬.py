def solution(nums):
    d = dict()
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    answer = min(len(d), len(nums)/2)
    return answer