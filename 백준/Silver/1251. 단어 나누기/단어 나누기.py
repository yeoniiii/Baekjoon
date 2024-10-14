from itertools import combinations

S = list(input())
words = []

for ij in combinations(range(len(S)), 2):
    i, j = ij
    a, b, c = S[:i], S[i:j], S[j:]
    if len(a) >= 1 and len(b) >= 1 and len(c) >= 1:
        a, b, c = a[::-1], b[::-1], c[::-1]
        words.append(''.join(a+b+c))
print(sorted(words)[0])