N = list(input())
F = int(input())

N[-2] = N[-1] = '0'
N = int(''.join(N))

q, r = divmod(N, F)

if r == 0: print('00')
else: print(str((q+1)*F)[-2:])