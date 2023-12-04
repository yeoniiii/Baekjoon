D, H, W = map(int, input().split())
k = (D**2 / (H**2 + W**2))**(1/2)
print(int(H*k), int(W*k))