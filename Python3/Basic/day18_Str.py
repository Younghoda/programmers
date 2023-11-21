# x 사이의 개수
# 문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(myString):
    answer = []
    myString = myString.split('x')
    for i in range(len(myString)):
        answer.append(len(myString[i]))
    return answer


# 문자열 잘라서 정렬하기
# 문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, 빈 문자열은 반환할 배열에 넣지 않습니다.
def solution(myString):
    answer = myString.split('x')
    answer = [element for element in  answer if element != '']
    answer.sort()
    return answer


# 간단한 식 계산하기
# 문자열 binomial이 매개변수로 주어집니다.
# binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다.
# 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.
def solution(binomial):
    answer = 0
    binomial = binomial.split(' ')
    if binomial[1] == '+':
        answer = int(binomial[0]) + int(binomial[2])
    elif binomial[1] == '-':
        answer = int(binomial[0]) - int(binomial[2])
    else:
        answer = int(binomial[0]) * int(binomial[2])
    return answer


# 문자열 바꿔서 찾기
# 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
# myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
def solution(myString, pat):
    answer = 0
    myString1 = ''
    for i in myString:
        if i == "A":
            myString1 += "B"
        elif i == "B":
            myString1 +=  "A"
        else:
            myString1 += i
    return int(pat in myString1)


# rny_string
# 'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다.
# 문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(rny_string):
    return rny_string.replace('m', 'rn')






