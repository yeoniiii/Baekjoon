N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))
rope.sort()
weight = 0
for i in range(N):
    weight_i = rope[i] * (N-i)
    if weight < weight_i:
        weight = weight_i
print(weight)