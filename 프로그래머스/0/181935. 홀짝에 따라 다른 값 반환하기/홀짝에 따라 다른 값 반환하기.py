def solution(n):
    r = 0
    if n % 2 == 1:   
        for i in range(1,n+1,2):
            r += i
    elif n % 2 == 0:
        for i in range(0,n+1,2):
            r += i**2
    return r
solution(8)
