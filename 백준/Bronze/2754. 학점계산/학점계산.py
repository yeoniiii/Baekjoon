score = input()
ans = ord('A') + 4 - ord(score[0])
if score[0] == 'F': ans += 1
elif score[1] == '+': ans +=0.3
elif score[1] == '-': ans -=0.3
print(float(ans))