N, M, B = map(int, input().split())
arr = [0] * 257

for i in range(N):
    arr_i = list(map(int, input().split()))
    for n in arr_i:
        arr[n] += 1

time, height = [], []

for h in range(256, -1, -1): # 기준 높이 (0~256)
    B_h, time_h = B, 0
    for i in range(257): # 인덱스
        if arr[i] > 0: # 개수가 1개 이상일 때 수행
            if h < i:
                time_h += 2 * arr[i] * (i-h) # 시간 * 개수 * 차이
                B_h += arr[i] * (i-h)
            elif h > i:
                time_h += 1 * arr[i] * (h-i) # 시간 * 개수 * 차이
                B_h -= arr[i] * (h-i)
    if B_h < 0:
        continue
    time.append(time_h)
    height.append(h)

print(min(time), height[time.index(min(time))])