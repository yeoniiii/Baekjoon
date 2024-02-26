P = [0] * 101
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(4, 101):
    P[i] = max(P[i-3] + P[i-2], P[i-1])
    
T = int(input())
for t in range(T):
    print(P[int(input())])