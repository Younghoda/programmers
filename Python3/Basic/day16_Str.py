# 대문자로 바꾸기
# 알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
def solution(myString):
    return myString.upper()


# 소문자로 바꾸기
# 알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
def solution(myString):
    return myString.lower()


# 배열에서 문자열 대소문자 변환하기
# 문자열 배열 strArr가 주어집니다.
# 모든 원소가 알파벳으로만 이루어져 있을 때, 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로,
# 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.
def solution(strArr):
    for i in range(len(strArr)):
        if i%2 ==1:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    return strArr


# A 강조하기
# 문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
def solution(myString):
    myString = myString.lower()
    myString = myString.replace('a', 'A')
    return myString


# 특정한 문자를 대문자로 바꾸기
# 영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때,
# my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


