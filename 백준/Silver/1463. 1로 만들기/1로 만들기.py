X = int(input())

num = [0]*(10**6 + 2)
num[2] = num[3] = 1

if X + 2 >= 4:
    for i in range(4, X+2):
        if (i % 2 == 0 and i % 3 != 0):
            num[i] = min(num[int(i/2)], num[i-1]) + 1
        elif (i % 2 != 0 and i % 3 == 0):
            num[i] = min(num[int(i/3)], num[i-1]) + 1
        elif (i % 2 == 0 and i % 3 == 0):
            num[i] = min(num[int(i/2)], num[int(i/3)], num[i-1]) + 1
        else:
            num[i] = num[int(i-1)] + 1
            
print(num[X])