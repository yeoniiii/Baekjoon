N, B = input().split()
ans = 0

for i in range(len(N)):
    if ord(N[i])>=ord('A'):
        Ni = ord(N[i])-55
    else: Ni = int(N[i])
    ans += Ni * (int(B)**(len(N)-i-1))
print(ans)