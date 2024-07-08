import sys
input = lambda: sys.stdin.readline().rstrip()

R, S = map(int, input().split())
arr = []
for r in range(R):
    arr.append(list(input()))

new_arr = [['.'] * S for r in range(R)]
move = R+1

for s in range(S):
    last_X = -1
    first_O = 3001
    flag = False
    for r in range(R):
        if arr[r][s] == 'X':
            last_X = max(last_X, r)
            flag = True
        elif arr[r][s] == '#':
            first_O = min(first_O, r)
    if flag:
        move = min(first_O-last_X-1, move)
        
for s in range(S):
    for r in range(R):
        if arr[r][s] == '#':
            new_arr[r][s] = '#'
        if arr[r][s] == 'X':
            new_arr[r+move][s] = 'X'
            
for r in range(R):
    for s in range(S):
        sys.stdout.write(new_arr[r][s])
    sys.stdout.write('\n')