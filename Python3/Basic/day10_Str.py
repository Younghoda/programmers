# 문자열의 앞의 n글자
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, n):
    return my_string[0:n]


# 접두사인지 확인하기
# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, is_prefix):
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[:i])
    for j in arr:
        if j == is_prefix:
            answer = 1
            break
        else:
            answer = 0
    return answer


# 문자열 뒤집기
# 문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, s, e):
    answer = ''
    str = my_string[s:e+1]
    answer = my_string[:s] + str[::-1] + my_string[e+1:]
    return answer

# 다른 풀이(my_string[s:e+1][::-1] 이런식으로도 할 수 있다,)


# 세로 읽기
# 문자열 my_string과 두 정수 m, c가 주어집니다.
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, m, c):
    answer = ''
    arr = []
    for i in range(int((len(my_string))/m)):
        arr.append(my_string[i*m:(i+1)*m])
    for j in arr:
        answer = answer+j[c-1]
    return answer

# 다른 풀이(c: 시작 인덱스를 나타내는 숫자, m: 간격을 나타내는 숫자)
def solution(s, m, c):
    return s[c-1::m]
def solution(my_string, m, c):
    answer = ''
    for i in range(c-1,len(my_string),m):
        answer+=my_string[i]
    return answer


# qr code
# 두 정수 q, r과 문자열 code가 주어질 때,
# code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer = answer + code[i]

    return answer


