from collections import deque

N = int(input())
arr = list(map(int, input().split()))

q = deque()
for i in range(1, N+1):
    q.append(i)
    
curr = q.popleft()
print(curr, end=" ")

while q:
    i = arr[curr-1]
    if i > 0:
        for j in range(i-1):
            q.append(q.popleft())
        curr = q.popleft()
        print(curr, end=" ")
    elif i < 0:
        for j in range(abs(i)-1):
            q.appendleft(q.pop())
        curr = q.pop()
        print(curr, end= " ")