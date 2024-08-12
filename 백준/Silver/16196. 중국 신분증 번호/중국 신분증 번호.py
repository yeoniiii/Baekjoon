import sys
input = lambda: sys.stdin.readline().rstrip()
import datetime

num = input()
N = int(input())

def valid_date(y, m, d):
    try:
        datetime.datetime(y, m, d)
        return True
    except ValueError:
        return False

code = []
for i in range(N):
    code.append(input())
if num[:6] not in code:
    print("I")
else:
    y = int(num[6:10])
    m = int(num[10:12])
    d = int(num[12:14])
    if y < 1900 or y > 2011 or m < 1 or m > 12 or d < 1 or d > 31:
        print("I")
    elif not valid_date(y, m, d):
        print("I")
    elif num[14:17] == '000':
        print("I")
    else:
        two = [2]
        for i in range(16):
            two.append(two[-1]*2)
        two = two[::-1]
        eq = 0
        for i in range(17):
            eq += int(num[i]) * two[i]
        if num[17] == 'X' and (eq + 10) % 11 != 1:
            print("I")
        elif num[17] != 'X' and (eq + int(num[17])) % 11 != 1:
            print("I")
        else:
            if int(num[16]) % 2 == 0:
                print("F")
            else:
                print("M")