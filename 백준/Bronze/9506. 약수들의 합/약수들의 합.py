def perfect(n):
    arr = []
    for i in range(2, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n-1 :
        print(f'{n} = 1', *arr, sep= " + ")
    else:
        print(n, 'is NOT perfect.')
          
while True:
    n = int(input())
    if n == -1:
        break
    perfect(n)