inp = []
for i in range(4):
    h, m = map(int, input().split(':'))
    m += 60*h
    inp.append(m)
if inp[0] < inp[1]:
    time1, time2, cycle1, cycle2 = inp
else:
    time2, time1, cycle2, cycle1 = inp
    
find = 0
while True:
    if time1 == time2:
        find = 1
        break
    elif time1 < time2:
        time1 += cycle1
    else:
        time2 += cycle2
    if time1 >= 10**6 and time2 >= 10**6:
        break
        
if find == 1:
    w, d = divmod(time1, 60*24*7)
    d, h = divmod(d, 60*24)
    h, m = divmod(h, 60)
    day = ['Satur', 'Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri']
    print(day[int(d)] + 'day')
    time = ''
    if len(str(h)) == 1:
        time += '0'
    time += str(h) + ':'
    if len(str(m)) == 1:
        time += '0'
    time += str(m)
    print(time)
else:
    print('Never')