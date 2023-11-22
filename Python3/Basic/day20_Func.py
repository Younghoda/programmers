# 배열의 길이를 2의 거듭제곱으로 만들기
# 정수 배열 arr이 매개변수로 주어집니다.
# arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
# arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    answer = []
    len_list=[1]
    i=1
    while (i<=1000):
        i = i*2
        len_list.append(i)
    if len(arr) in len_list:
        return arr
    else:
        for i in len_list:
            if i - len(arr) >0:
                for j in range(i - len(arr)):
                    arr.append(0)
                return arr

# 다른 풀이(while문을 사용)
def solution(arr):
    answer = [2**i for i in range(11)]
    while len(arr) not in answer:
        arr.append(0)
    return arr


# 배열 비교하기
# 이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.
# 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
# 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
# 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(arr1, arr2):
    sum1=0
    sum2=0

    if (len(arr1)) != (len(arr2)):
        if len(arr1)>len(arr2):
            answer = 1
        else:
            answer = -1
    else:
        for i in range(len(arr1)):
            sum1 += arr1[i]
            sum2 += arr2[i]
        if sum1 == sum2:
            answer = 0
        else:
            if sum1 > sum2:
                answer = 1
            else:
                answer = -1
    return answer


# 문자열 묶기
# 문자열 배열 strArr이 주어집니다.
# strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
def solution(strArr):
    answer = 0
    str_list = []
    for i in strArr:
        str_list.append(len(i))

    most_common_number = max(set(str_list), key=str_list.count)
    count_most_common = str_list.count(most_common_number)
    return count_most_common

# 다른 풀이
def solution(strArr):
    answer = 0
    arr = [0] * 31
    for i in strArr:
        arr[len(i)] += 1
    return max(arr)


# 배열의 길이에 따라 다른 연산하기
# 정수 배열 arr과 정수 n이 매개변수로 주어집니다.
# arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr, n):
    if len(arr) % 2==1:
        for i, s in enumerate(arr):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i, s in enumerate(arr):
            if i % 2 == 1:
                arr[i] += n
    return arr


# 뒤에서 5등까지
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    num_list.sort()
    num_list = num_list[:5]
    return num_list






