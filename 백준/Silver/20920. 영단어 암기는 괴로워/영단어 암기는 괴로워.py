import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
vocab = {}

for i in range(N):
    inp = input()
    if len(inp) >= M:
        if inp in vocab:
            vocab[inp] += 1
        else:
            vocab[inp] = 1

vocab_list = sorted(vocab, key=lambda x: (-vocab[x], -len(x), x))
for v in vocab_list:
    print(v)