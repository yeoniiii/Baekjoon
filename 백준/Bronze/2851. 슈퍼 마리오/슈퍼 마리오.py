s = 0
min_d = 101
max_s = 0
for i in range(10):
    m = int(input())
    s += m
    if abs(s - 100) <= min_d:
        if max_s <= s:
            min_d = abs(s-100)
            max_s = s
        
print(max_s)