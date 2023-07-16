arr = []
for _ in range(5):
    arr.append(int(input()))
arr.sort()
    
print(int(sum(arr)/5), int(arr[2]), sep='\n')