while True:
    num = int(input())
    if num == 0:
        break
    if len(str(num)) == 1:
        print(num)
        continue
    while True:
        new_num = sum(map(int, list(str(num))))
        if len(str(new_num)) == 1:
            print(new_num)
            break
        num = new_num