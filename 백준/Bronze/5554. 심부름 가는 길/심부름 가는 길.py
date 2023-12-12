arr = []
for i in range(4):
    arr.append(int(input()))
x, y = divmod(sum(arr), 60)
print(x, y, sep='\n')