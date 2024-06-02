import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
stack = []
for i in range(N):
    stack.append(int(input()))

view = [stack.pop()]

while stack:
    s = stack.pop()
    if s > view[-1]:
        view.append(s)
        
print(len(view))