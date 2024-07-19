S = input()
d = ['aespa', 'baekjoon', 'cau', 'debug', 'edge', 'firefox', 'golang', 'haegang', 'iu', 'java', 'kotlin', 'lol', 'mips', 'null', 'os',
     'python', 'query', 'roka', 'solvedac', 'tod', 'unix', 'virus', 'whale', 'xcode', 'yahoo', 'zebra']
S_HG = ''
ans = []
s_idx = 0
error = 0
while s_idx < len(S):
    d_idx = ord(S[s_idx]) - ord('a')
    ans.append(S[s_idx])
    if d[d_idx] != S[s_idx : s_idx+len(d[d_idx])]:
        error = 1
        break
    s_idx += len(d[d_idx])
if error == 0:
    print("It's HG!")
    print(*ans, sep='')
else:
    print('ERROR!')