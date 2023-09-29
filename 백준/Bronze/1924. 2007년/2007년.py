x, y = map(int, input().split())
m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(x):
    y += m[i]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(week[y % 7 - 1])