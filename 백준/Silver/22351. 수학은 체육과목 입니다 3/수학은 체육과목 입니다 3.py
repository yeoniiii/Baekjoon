S = input()

d = 1
find = 0
start = end = -1

while True:
    start = int(S[:d])
    s = str(start) + str(start+1)
    if len(s) > len(S):
        break
    if s == S[:len(s)]:
        find = 1
        break
    d += 1

if find == 0:
    start = end = int(S)
else:
    i = start
    s = str(i)
    while i < 999:
        s += str(i+1)
        if len(s) == len(S):
            if s == S:
                find += 1
                end = i + 1
                break
        i += 1

    if end == -1:
        start = end = int(S)

print(start, end)