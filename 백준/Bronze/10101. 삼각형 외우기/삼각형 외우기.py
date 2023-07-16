angle = []
for i in range(3):
    angle.append(int(input()))
angle.sort()
an = sorted(list(set(angle)))

if sum(angle) != 180: print("Error")
elif angle[0] == angle[1] == 60: print("Equilateral")
elif angle == an: print("Scalene")
else: print("Isosceles")