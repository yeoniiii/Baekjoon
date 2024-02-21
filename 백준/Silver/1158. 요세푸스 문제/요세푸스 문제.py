from collections import deque

N, K = map(int, input().split())

queue = deque()
for i in range(N):
    queue.append(i+1)
curr = queue[K-1]
ans = '<'

while queue:
    if queue[0] == curr:
        ans += str(queue[0])+', '
        queue.popleft()
        if queue:
            curr = queue[(K-1) % len(queue)]
    else:
        queue.append(queue.popleft())

print(ans[:-2] + '>')