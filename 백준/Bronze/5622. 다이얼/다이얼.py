word = input()
arr = [ord(i) for i in word]
time = 0
for num in arr:
    if num <= ord('O'):
        time += (num-65)//3 + 3
    elif num in range(ord('P'), ord('S')+1):
        time += 7+1
    elif num in range(ord('T'), ord('V')+1):
        time += 8+1
    else :
        time += 9+1
print(time)