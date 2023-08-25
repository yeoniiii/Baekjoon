N, M = map(int, input().split())
card = list(map(int, input().split()))
max = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            s = card[i] + card[j] + card[k]
            if s >= max and s <= M:
                max = s
print(max)