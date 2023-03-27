arr = [i.upper() for i in input()]
uniq = list(set(arr))

max_cnt = 0
cnt = [arr.count(i) for i in uniq]
max_cnt = max(cnt)
if cnt.count(max_cnt) >= 2: max_i='?'
else : max_i = uniq[cnt.index(max_cnt)]
print(max_i)