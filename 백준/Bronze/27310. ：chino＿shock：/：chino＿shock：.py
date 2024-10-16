emoji = input()
colon, bar = 0, 0
for e in emoji:
    if e == ':':
        colon += 1
    elif e == '_':
        bar += 1
print(len(emoji)+colon+bar*5)