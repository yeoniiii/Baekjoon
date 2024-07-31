S, M = map(int, input().split())
if S <= 1023:
    print('No thanks')
elif (S - 1023) & M == (S - 1023):
    print('Thanks')
else:
    print('Impossible')