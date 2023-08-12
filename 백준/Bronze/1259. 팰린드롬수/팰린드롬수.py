import sys
while True:
    num = sys.stdin.readline().rstrip()
    if num == '0': break
    elif num == num[::-1]: print('yes')
    else: print('no')