num = 0
pay = 1000 - int(input())
yen = [500, 100, 50, 10, 5, 1]
for y in yen:
    num += pay // y
    pay = pay % y

print(num)