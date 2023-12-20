def solution(n):
    answer = 0
    
    for i in range(10,0,-1):
        factorial=1
        for j in range(1,i+1):
            factorial *= j
        if factorial <= n:
            return i