A = int(input())
X = int(input())

arr = [A]
exp = 1
while True:
    exp *= 2
    if X < exp:
        break
    arr.append((arr[-1] ** 2) % 1000000007)
    
def decompose_bin(x):
    result = []
    power = 0
    
    while x > 0:
        if x % 2 == 1:
            result.append(power)
        x //= 2
        power += 1
        
    return result

def solution(A, X):
    X_bin = decompose_bin(X)

    ans = 1
    for b in X_bin:
        ans *= (arr[b])
    return ans % 1000000007
    
print(solution(A, X))