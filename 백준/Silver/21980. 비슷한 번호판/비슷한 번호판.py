from itertools import combinations

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    numbers = input().split()

    # Insert code here
    rule = []
    for number in numbers:
        upp = 0
        for num in number:
            if num.isupper():
                upp += 1
        rule.append(str(upp) + ''.join(sorted(number.lower())))

    d = {}
    for r in rule:
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for key, val in d.items():
        if val >= 2:
            ans += val*(val-1)//2
    
    print(ans)