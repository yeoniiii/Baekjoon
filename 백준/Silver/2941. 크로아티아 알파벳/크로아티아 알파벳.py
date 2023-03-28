inp = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in cro:
    if i in inp:
        cnt += inp.count(i)
print(len(inp)-cnt)