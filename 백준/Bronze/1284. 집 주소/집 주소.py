def wid(x):
    n = len(x)
    width = n + 1
    for i in range(n):
        if x[i] == '1':
            width += 2
        elif x[i] == '0':
            width += 4
        else:
            width += 3
    return width

while True:
    num = input()
    if num == '0': break
    print(wid(num))