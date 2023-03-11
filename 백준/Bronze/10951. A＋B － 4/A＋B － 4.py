import sys

while True:
    try :
        inp = input()
        print(sum(map(int, inp.split())))
        if inp=="":
            break
    except :
        break