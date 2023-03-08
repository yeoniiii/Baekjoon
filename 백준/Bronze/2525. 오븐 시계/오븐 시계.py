h, m = map(int, input().split())
t = int(input())

time = h*60 + m + t

h, m = divmod(time, 60)

if h>=24 : print(h-24, m)
else : print(h, m)