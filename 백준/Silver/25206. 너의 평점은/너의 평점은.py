score_sum = credit_sum = 0
for i in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade[0] == 'A': score = 4.0
    elif grade[0] == 'B': score = 3.0
    elif grade[0] == 'C': score = 2.0
    elif grade[0] == 'D': score = 1.0
    if grade == 'F': score = 0.0
    elif grade == 'P': score = credit = 0.0
    elif grade[1] == '+' : score += 0.5

    score_sum += credit * score
    credit_sum += credit

print(score_sum / credit_sum)