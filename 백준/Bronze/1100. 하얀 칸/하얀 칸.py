ans = 0

for i in range(8):
    chess = list(input())
    if i % 2 == 0:
        for j in range(4):
            if chess[2*j] == 'F':
                ans += 1
    else:
        for j in range(4):
            if chess[2*j + 1] == 'F':
                ans += 1
                
print(ans)