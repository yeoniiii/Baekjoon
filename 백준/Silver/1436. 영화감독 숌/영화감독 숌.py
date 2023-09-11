arr = []
for i in range(10000000):
    if '666' in str(i): arr.append(i)
    if len(arr) == 10000: break
print(arr[int(input())-1])