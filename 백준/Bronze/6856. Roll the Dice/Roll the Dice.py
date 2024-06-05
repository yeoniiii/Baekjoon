n = int(input())
m = int(input())

if n + m == 10:
    print(f"There is 1 way to get the sum 10.")
else:
    num = 0
    for i in range(1, 10):
        if i <= n and (10-i) <= m:
            num += 1
    print(f"There are {num} ways to get the sum 10.")