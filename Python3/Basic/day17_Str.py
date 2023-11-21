########################################### 다시 풀어보기 ######################################
# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# 문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.
def solution(myString, pat):
    idx = myString.rfind(pat)
    return myString[:idx+len(pat)]


# 문자열이 몇 번 등장하는지 세기
# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
def solution(myString, pat):
    answer = 0
    while (pat in myString):
        answer += 1
        idx = myString.find(pat)
        myString = myString[idx+1:]
    return answer


# ad 제거하기
# 문자열 배열 strArr가 주어집니다.
# 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.
def solution(strArr):
    answer = []
    for i in strArr:
        if not('ad' in i):
            answer.append(i)
    return answer

# 또 다른 풀이
def solution(strArr):
    return [s for s in strArr if 'ad' not in s]


########################################### 다시 풀어보기 ######################################
# 공백으로 구분하기 1
# 단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
# my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    return my_string.split(' ')


# 공백으로 구분하기 2
# 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
# my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    return my_string.split()

# 또 다른 풀이
def solution(my_string):
    return [i for i in my_string.split(" ") if i != ""]





