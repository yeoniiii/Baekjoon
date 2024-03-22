from itertools import permutations

def solution(k, dungeons):
    answer = []
    for perm in permutations(range(len(dungeons)), len(dungeons)):
        curr_k = k
        cnt = 0
        for i in perm:
            need_k, use_k = dungeons[i]
            if curr_k >= need_k:
                curr_k -= use_k
                cnt += 1
            answer.append(cnt)
    return max(answer)