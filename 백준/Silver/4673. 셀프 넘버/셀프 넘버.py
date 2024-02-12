arr = []
for i in range(1, 10001):
    i_sum = i
    for j in range(len(str(i))):
        i_sum += int(str(i)[j])
    arr.append(i_sum)
for i in range(1, 10001):
    if i in arr:
        pass
    else:
        print(i)