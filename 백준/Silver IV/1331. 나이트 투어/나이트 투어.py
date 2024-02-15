import sys
input = lambda: sys.stdin.readline().rstrip()

def loc_to_coord(loc):
    return [int(ord(loc[0]) - ord('A') + 1), int(loc[1])]

def check_next(new, past):
    global visited
    if abs(new[0] - past[0]) == 2 and abs(new[1] - past[1]) == 1:
        return True
    elif abs(new[0] - past[0]) == 1 and abs(new[1] - past[1]) == 2:
        return True   
    else:
        return False

loc = loc0 = loc_to_coord(input())
visited = [[0]*6 for _ in range(6)]
visited[loc[0]-1][loc[1]-1] += 1

for i in range(35):
    new_loc = loc_to_coord(input())
    
    if visited[new_loc[0]-1][new_loc[1]-1] == 0 and check_next(new_loc, loc):
        loc = new_loc
        visited[loc[0]-1][loc[1]-1] += 1
    else:
        break

is_zero = 0
for i in range(6):
    is_zero += int(0 in visited[i])
    
if is_zero == 0 and check_next(loc, loc0):
    print("Valid")
else:
    print("Invalid")