# n 번째 원소부터
# 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    answer = num_list[n-1:]
    return answer


# 순서 바꾸기
# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    arr1 = num_list[:n]
    arr2 = num_list[n:]
    return arr2+arr1


# 왼쪽 오른쪽
# 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다.
# str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를,
# 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# "l"이나 "r"이 없다면 빈 리스트를 return합니다.
def solution(str_list):
    answer = []
    for i, s in enumerate(str_list):
        if s == 'l':
            return str_list[:i]
        elif s == 'r':
            return str_list[i+1:]
    return answer


# n 번째 원소까지
# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    return num_list[:n]


# n개 간격의 원소들
# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    return num_list[::n]





