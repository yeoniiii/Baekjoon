S = input()
stack = []
open = {'(':1, '{':2, '[':3}
close = {')':1, '}':2, ']':3}
b = 0
score = 0
for s in S:
    if s in close:
        score -= close[s]
    elif s in open:
        score += open[s]
    else:
        if b < score:
            b = score

print(b)