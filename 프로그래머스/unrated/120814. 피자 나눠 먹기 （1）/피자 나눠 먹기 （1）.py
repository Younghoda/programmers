def solution(n):
    for i in range(15):
        if 7*i <= n <= 7*(1+i):
            return i+1
