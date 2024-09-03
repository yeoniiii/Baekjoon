S = ''

while True:
    try:
        S += input()
    except:
        break
      
d = {}
for s in S:
    if s == ' ':
        continue
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

ans = []
max_num = max(d.values())
for key, val in d.items():
    if val == max_num:
        ans.append(key)
print(''.join(sorted(ans)))