A, B = map(int, input().split())
print(int(str(A).replace('6', '5'))+int(str(B).replace('6', '5')),
     int(str(A).replace('5', '6'))+int(str(B).replace('5', '6')))