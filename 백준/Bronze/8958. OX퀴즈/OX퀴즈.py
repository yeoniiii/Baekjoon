N = int(input())

for _ in range(N):
    test = list(input())
    for i in range(len(test)):
        score = c = 0
        for i in range(len(test)):
            if test[i] == 'O': 
                c += 1
                score += c
            else:
                c = 0
    print(score)