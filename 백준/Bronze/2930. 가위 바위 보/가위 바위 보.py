import sys
input = lambda: sys.stdin.readline().rstrip()

rule = {'SP':2, 'PR':2, 'RS':2,
        'SS':1, 'PP':1, 'RR':1,
        'PS':0, 'RP':0, 'SR':0}

R = int(input())
sang = input()
N = int(input())
friends = []
score, max_score = 0, 0
for n in range(N):
    friends.append(input())
for r in range(R):
    scores = {'S':0, 'P':0, 'R':0}
    for s in scores.keys():
        for n in range(N):
            scores[s] += rule[s+friends[n][r]]
    score += scores[sang[r]]
    max_score += max(scores.values())
print(score)
print(max_score)