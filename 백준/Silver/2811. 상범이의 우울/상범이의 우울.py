N = int(input())
feel = list(map(int, input().split()))
T = {}

i = 0
while i < N:
    if feel[i] < 0:
        j = 1
        while i+j < N:
            if feel[i+j] >= 0:
                break
            j += 1
        T[i] = j
        i += j
    else:
        i += 1

def calculate_flower(T_max_start):
    flower = [0] * N

    for key, val in T.items():
        if val == T_max and key == T_max_start:
            f = min(key, 3*val)
        else:
            f = min(key, 2*val)

        for idx in range(key-f, key):
            flower[idx] = 1
    
    return sum(flower)


if T:
    T_max = max(T.values())
    T_max_starts = []
    for key, val in T.items():
        if val == T_max:
            T_max_starts.append(key)

    flowers = []
    for T_max_start in T_max_starts:
        flowers.append(calculate_flower(T_max_start))

    print(max(flowers))

else:
    print(0)