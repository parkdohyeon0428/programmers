def solution(ineq, eq, n, m):
    result = 0
    if (ineq == ">" and eq == "="):
   
        if n >= m:
            result = 1
        else:
            result = 0
    
    elif (ineq == "<" and eq == "="):
        if n <= m:
            result = 1
        else:
            result = 0
    
    elif (ineq == ">" and eq == "!"):
        if n > m:
            result = 1
        else:
            result = 0
    
    elif (ineq == "<" and eq == "!"):
        if n < m:
            result = 1
        else:
            result = 0
    return result
solution("<", "=", 5, 6)