def solution(a, b):
    max_i = 0
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0 and max_i < i:
            max_i = i
    m = a//max_i
    n = b//max_i
    return max_i * m * n

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(solution(a, b))