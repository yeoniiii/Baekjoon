T = int(input())
for t in range(T):
    blank = input()
    S = sorted(list(input()), reverse=True)
    num2 = int(S.pop())
    num1 = int(''.join(S))
    print(num1 + num2)