N = int(input())
S = input()

bitamin = False
for l in range(1, N+1):
    diff = 0
    for i in range(l):
        if S[i] == S[-l+i]:
            continue
        diff += 1
        
    if diff == 1:
        bitamin = True
        break

if bitamin:
    print('YES')
else:
    print('NO')