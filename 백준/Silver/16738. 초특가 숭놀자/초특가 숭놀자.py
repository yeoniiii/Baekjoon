import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
room = [0] * N
people = []
new = 0
for q in range(Q):
    command, A, B = input().split()
    A, B = int(A), int(B)
    
    if command == 'new':
        rejected = True
        for n in range(N):
            if room[n:(n+B)] == [0]*B:
                new += 1
                rejected = False
                room[n:(n+B)] = [new]*B
                people.append(A)
                break
        if rejected:
            print('REJECTED')
        else:
            print(n+1, n+B)
                
    elif command == 'in':
        people[A-1] += B
    elif command == 'out':
        people[A-1] -= B
        if people[A-1] == 0:
            clean = []
            for n in range(N):
                if room[n] == A:
                    room[n] = 0
                    clean.append(n)
            print('CLEAN', min(clean)+1, max(clean)+1)