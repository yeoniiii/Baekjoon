def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for l in lost[:]:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
            
    return n - len(lost)