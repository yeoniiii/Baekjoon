import heapq

def solution(scoville, K):
    answer = 0
    s = []
    for i in scoville:
        heapq.heappush(s, i)
    while s[0] < K and len(s) > 1:
        a = heapq.heappop(s)
        b = heapq.heappop(s)
        heapq.heappush(s, a+b*2)
        answer += 1
    if len(s) == 1 and s[0] < K:
        return -1
    return answer