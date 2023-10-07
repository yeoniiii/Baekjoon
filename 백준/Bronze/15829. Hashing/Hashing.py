L = int(input())
arr = list(input())
s = 0

for i in range(L):
    n = ord(arr[i])-ord('a')+1
    s += n*31**i
print(s%1234567891)