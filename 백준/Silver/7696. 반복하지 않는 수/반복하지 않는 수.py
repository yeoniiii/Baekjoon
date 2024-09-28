import sys
input = lambda: sys.stdin.readline().rstrip()

inputs = []
while True:
    n = int(input())
    if n == 0:
        break
    inputs.append(n)
    
until = max(inputs)
output = []
for i in range(1, 10000000000):
    str_i = str(i)
    if len(set(str_i)) == len(str_i):
        output.append(i)
    if len(output) == until:
        break

for i in inputs:
    print(output[i-1])