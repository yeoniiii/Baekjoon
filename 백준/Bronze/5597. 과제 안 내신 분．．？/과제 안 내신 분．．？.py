std = []
for i in range(28):
    std.append(int(input()))
std = set(std)

std_all = set([i+1 for i in range(30)])
no = list(std_all - std)
no.sort()

print(no[0])
print(no[1])