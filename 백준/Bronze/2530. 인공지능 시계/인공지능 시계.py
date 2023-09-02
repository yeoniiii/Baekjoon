A, B, C = map(int, input().split())
D = int(input())
time = A*3600 + B*60 + C + D
H, time = divmod(time, 3600)
M, S = divmod(time, 60)
print(H%24, M, S)