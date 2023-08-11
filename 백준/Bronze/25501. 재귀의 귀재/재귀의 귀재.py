def recursion(s, l, r):
    global n # UnboundLocalError: local variable 'n' referenced before assignment 방지
    n += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for _ in range(T):
    n = 0
    S = input()
    print(isPalindrome(S), n)