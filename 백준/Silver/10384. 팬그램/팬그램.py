n = int(input())

for i in range(n):
    d = {}
    for c in range(ord('a'), ord('z')+1):
        d[chr(c)] = 0
        
    S = input()
    for s in S:
        if s.lower() in d:
            d[s.lower()] += 1
            
    one, double, triple = 0, 0, 0
    for key, value in d.items():
        if value >= 3:
            triple += 1
        if value >= 2:
            double += 1
        if value >= 1:
            one += 1

    if triple == 26:
        print(f"Case {i+1}: Triple pangram!!!")
    elif double == 26:
        print(f"Case {i+1}: Double pangram!!")
    elif one == 26:
        print(f"Case {i+1}: Pangram!")
    else:
        print(f"Case {i+1}: Not a pangram")
        