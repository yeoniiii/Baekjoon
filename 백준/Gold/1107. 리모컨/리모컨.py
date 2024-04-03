import heapq

N = int(input())
M = int(input())
inp = ""
while True:
    try:
        inp = input()
    except EOFError:
        break
no = list(map(int, inp.split()))

q = []

# 숫자 없이 +, -로만 이동했을 때
cnt = abs(N-100)

if M == 10:
    print(cnt)

else:
    heapq.heappush(q, cnt)

    for i in range(1000000):
        temp = True
        for j in str(i):
            if int(j) in no:
                temp = False
                break
        if temp == True:
            heapq.heappush(q, len(str(i)) + abs(N-i))
        
    print(heapq.heappop(q))