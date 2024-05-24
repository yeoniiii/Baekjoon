A, B, C = map(int, input().split())

arr = [A]
exp = 1
while True:
    exp *= 2
    if B < exp:
        break
    arr.append((arr[-1] ** 2) % C)
    
def decompose_bin(x):
    result = []
    power = 0
    
    while x > 0:
        if x % 2 == 1:
            result.append(power)
        x //= 2
        power += 1
     
    return result

B_bin = decompose_bin(B)
ans = 1
for b in B_bin:
    ans *= arr[b]
    
print(ans % C)