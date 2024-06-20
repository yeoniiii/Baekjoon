import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = set()
for i in range(N):
    words.add(input())

M = int(input())
for m in range(M):
    no = []
    while True:
        e = input()
        if e == '-1':
            if len(no) == 0:
                print(f"Email {1+m} is spelled correctly.")
            else:
                print(f"Email {1+m} is not spelled correctly.")
                print(*no, sep='\n')
            break
        elif e not in words:
            no.append(e)
print("End of Output")