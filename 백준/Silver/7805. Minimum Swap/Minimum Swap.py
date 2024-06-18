import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    S = input()
    N = len(S)
    if S:
        case = []
        for i in range(N):
            case.append((S[i], i))
        case.sort()

        visited = [0] * N
        swap = 0

        for i in range(N):
            if visited[i] == 1:
                continue

            cycle = 0
            v = i

            while visited[v] == 0:
                visited[v] = 1
                cycle += 1
                v = case[v][1]

            swap += cycle - 1

        print(swap)
   
    else:
        break