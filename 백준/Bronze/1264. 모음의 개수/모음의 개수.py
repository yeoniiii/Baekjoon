vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    eng = input()
    if eng == "#": break
    else:
        s = 0
        for e in range(len(eng)):
            if eng[e] in vowel: s += 1
        print(s)