rule = {'AA':'A', 'AG':'C', 'AC':'A', 'AT':'G',
       'GG':'G', 'GC':'T', 'GT':'A',
       'CC':'C', 'CT':'G', 'TT':'T'}
for r in ['GA', 'CA', 'CG', 'TG', 'TA', 'TC']:
    a, b = r[0], r[1]
    rule[r] = rule[b+a]

N = int(input())
seq = list(input())
while len(seq) > 1:
    b = seq.pop()
    a = seq.pop()
    seq.append(rule[a+b])
print(seq[0])