while True:
    name, age, kg = input().split()
    if name == '#':
        break
    elif (int(age) > 17) | (int(kg) >= 80): 
        print(name, 'Senior')
    else: print(name, 'Junior')