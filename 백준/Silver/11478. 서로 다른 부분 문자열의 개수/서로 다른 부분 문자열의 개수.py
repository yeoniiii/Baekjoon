S = input()

arr = set()


for i in range(len(S)):
    j = 1
    while i+j <= len(S):
        arr.add(S[i:(i+j)])
        j+= 1
        
print(len(arr))