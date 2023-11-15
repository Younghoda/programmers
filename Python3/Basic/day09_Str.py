# 배열 만들기 5
# 문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
# 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다.
# 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(intStrs, k, s, l):
    answer1 = []
    answer=[]
    for i in intStrs:
        answer1.append(int(i[s:s+l]))
    for j in answer1:
        if j > k:
            answer.append(j)
    return answer

# 다른 풀이
def solution(intStrs, k, s, l):
    return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]


# 부분 문자열 이어 붙여 문자열 만들기
# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_strings, parts):
    answer = ''
    count=0
    for s,e in parts:
        answer = answer + my_strings[count][s:e+1]
        count += 1
    return answer

# 다른 풀이(이차원 정수 배열에 enumerate를 사용한 반복문 사용법 = for i, (s, e) in enumerate(parts):)
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer


# 문자열의 뒤의 n글자
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, n):
    answer = ''
    answer = answer + my_string[len(my_string)-n:]
    return answer

# 다른 풀이 ([-n:] -> 뒤에서 n만큼 이동한 후 끝까지)
def solution(my_string, n):
    return my_string[-n:]


# 접미사 배열
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    answer.sort()
    return answer

# 접미사인지 확인하기
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, is_suffix):
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[i:])
    for j in arr:
        if j == is_suffix:
            answer = 1
            break
        else:
            answer = 0
    return answer


