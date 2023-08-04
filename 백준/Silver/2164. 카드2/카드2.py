from collections import deque
N = int(input())
queue = deque(list(range(1, N+1)))

while len(queue) >= 3:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[-1])