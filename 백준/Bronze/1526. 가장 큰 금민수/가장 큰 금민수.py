N = int(input())
for i in range(N, 3, -1):
    no = 0
    for j in str(i):
        if j not in ['4', '7']:
            no += 1
            break
    if no == 0:
        answer = i
        break
print(answer)