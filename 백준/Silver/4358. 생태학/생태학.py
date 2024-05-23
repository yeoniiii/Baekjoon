import sys
input = lambda: sys.stdin.readline().rstrip()
d = {}
num = 0

while True:
    data = input()
    if data == '':
        break
    else:
        if data in d:
            d[data] += 1
        else:
            d[data] = 1
        num += 1
        
for key in sorted(d.keys()):
    p = d[key] / num * 100
    print(f"{key} {p:.4f}")