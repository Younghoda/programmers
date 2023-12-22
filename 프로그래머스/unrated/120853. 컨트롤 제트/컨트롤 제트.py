def solution(s):
    answer = 0
    s = s.split(" ")
    for e, i in enumerate(s):
        if i == "Z":
            answer -= int(s[e-1])
        else:
            answer += int(i)
        
    return answer