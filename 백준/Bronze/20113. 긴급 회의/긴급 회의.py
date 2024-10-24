N = int(input())
X = list(map(int, input().split()))
skip = 0
d = {}
for x in X:
    if x == 0:
        skip += 1
    elif x in d:
        d[x] += 1
    else:
        d[x] = 1
        
max_vote = max(d.values())
imposter = []
for key, val in d.items():
    if val == max_vote:
        imposter.append(key)
if len(imposter) == 1:
    print(imposter[0])
else:
    print('skipped')