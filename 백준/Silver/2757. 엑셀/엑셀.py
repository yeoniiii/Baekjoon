import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    inp = input()
    if inp == "R0C0":
        break
    ans = ''
    r, c = inp.split('C')
    a = int(c)
    while a > 26:
        a, b = divmod(a - 1, 26)
        ans += chr(b + ord('A'))
    ans += chr(a + ord('A') - 1)
    ans = ans[::-1] + r[1:]
    print(ans)