A, B = map(int, input().split())
cnt = 0
if A % 2 == 0:
    cnt += 1
    A += 1
if B % 2 == 1:
    cnt += 1
    B -= 1
cnt += ((B+1) - A)//2
print(cnt)