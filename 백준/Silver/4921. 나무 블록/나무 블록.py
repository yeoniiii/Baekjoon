import sys
input = lambda: sys.stdin.readline().rstrip()
nxt = [[], [4, 5], [], [4, 5], [2, 3], [8], [2, 3], [8], [6, 7]]
n = 1

while True:
    tc = input()
    if tc == '0':
        break
        
    valid = True
    if tc[0] == '1' and tc[-1] == '2':
        for i in range(1, len(tc)):
            if int(tc[i]) not in nxt[int(tc[i-1])]:
                valid = False
                break
    else:
        valid = False
        
    if valid:
        print(f'{n}. VALID')
    else:
        print(f'{n}. NOT')
    
    n += 1