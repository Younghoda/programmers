# 조건에 맞게 수열 변환하기 1
# 정수 배열 arr가 주어집니다.
# arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i/2)
        elif i <50 and i%2 ==1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer


########################################### 다시 풀어보기 ######################################
# 조건에 맞게 수열 변환하기 2
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.
# 이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.
# 단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.
def solution(arr):
    x = 0
    prev = arr
    while 1:
        arrx = []
        for s in prev:
            if s >= 50 and s % 2 == 0:
                arrx.append(s / 2)
            elif s < 50 and s % 2 == 1:
                arrx.append(s * 2 + 1)
            else:
                arrx.append(s)

        same = all(a == b for a, b in zip(prev, arrx))

        if same:
            break
        x += 1

        prev = arrx
    return x


########################################### 다시 풀어보기 ######################################
# 1로 만들기
# 정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.
# 10 / 2 = 5
# (5 - 1) / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# 위와 같이 4번의 나누기 연산으로 1이 되었습니다.
# 정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = 0

    for i in num_list:
        cnt = 0
        while i > 1:
            if i % 2 == 0:
                i = i // 2
            else:
                i = (i - 1) // 2

            # if int(i) == 1:
            #     break
            cnt += 1
        answer += cnt
    return answer


# 길이에 따른 연산
# 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = 1
    if len(num_list)>=11:
        for i in num_list:
            answer += i
        return (answer -1)
    else:
        for i in num_list:
            answer *= i
        return answer


# 원하는 문자열 찾기
# 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.
# 단, 알파벳 대문자와 소문자는 구분하지 않습니다.
def solution(myString, pat):
    answer = 0
    a = len(pat)
    for i in range(len(myString)-a+1):
        if pat.upper() == myString[i:i+a].upper():
            return 1
    return answer

# 다른 풀이
def solution(myString, pat):
    return int(pat.lower() in myString.lower())






