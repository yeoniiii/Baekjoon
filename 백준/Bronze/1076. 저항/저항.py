color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

s = 0
om = []

for i in range(3):
    om.append(color.index(input()))

print(int(str(om[0])+str(om[1])) * (10**om[2]))