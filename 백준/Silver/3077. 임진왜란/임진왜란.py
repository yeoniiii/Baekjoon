from itertools import combinations

N = int(input())
answer = list(input().split(' '))
d = {}
for i in range(N):
    d[answer[i]] = i
hyunwoo = list(input().split(' '))

answer = 0
for pair in combinations(range(N), 2):
    i, j = pair
    a, b = hyunwoo[i], hyunwoo[j]
    if d[a] < d[b]:
        answer += 1
        
print(str(answer)+'/'+str(N*(N-1)//2))