import random

N = int(input())
alphabets = []
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(ord('a'), ord('z')+1):
    if chr(i) not in vowels:
        alphabets.append(chr(i))

S = set()

while len(S) < N:
    l = random.sample(range(3, 21), 1)
    sample = []
    while True:
        if len(sample) >= l[0]:
            break
        sample += random.sample(alphabets, 1)
        if len(sample) >= l[0]:
            break
        sample += random.sample(alphabets, 1)
        if len(sample) >= l[0]:
            break
        sample += random.sample(vowels, 1)
        if len(sample) >= l[0]:
            break
        sample += random.sample(vowels, 1)
    name = ''.join(sample)
    
    if name not in S:
        S.add(name)

for s in S:
    print(s)