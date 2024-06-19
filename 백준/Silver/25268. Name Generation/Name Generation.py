C = "bcdfghjklmnpqrstvwxyz"
V = "aeiou"

def name(N):
    for a in C:
        for b in V:
            for c in C:
                for d in C:
                    if N == 0:
                        return 
                    N -= 1
                    print(a+b+c+d)
        
N = int(input())
name(N)