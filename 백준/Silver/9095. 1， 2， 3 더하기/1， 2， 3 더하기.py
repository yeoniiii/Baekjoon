num = [0]*10
num[0] = 1
num[1] = 2
num[2] = 4

for i in range(3, 10):
    num[i] = num[i-3] + num[i-2] + num[i-1]

T = int(input())
for i in range(T):
    print(num[int(input())-1])