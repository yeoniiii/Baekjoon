yd = input()
N = int(input())
names = []
probs = []
for i in range(N):
    name = input()
    names.append(name)
    
    name_ls = list(yd+name)
    L = name_ls.count('L')
    O = name_ls.count('O')
    V = name_ls.count('V')
    E = name_ls.count('E')
    
    probs.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
    
max_prob = max(probs)
max_names = []
for i in range(N):
    if probs[i] == max_prob:
        max_names.append(names[i])
        
print(sorted(max_names)[0])