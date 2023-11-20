# 홀수 vs 짝수
# 정수 리스트 num_list가 주어집니다.
# 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요.
# 두 값이 같을 경우 그 값을 return합니다.
def solution(num_list):
    answer1 = 0
    answer2 = 0
    for i in num_list[::2]:
        answer1 += i
    for i in num_list[1::2]:
        answer2 += i
    if answer1 > answer2:
        return answer1
    else:
        return answer2

# 다른 풀이
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))


# 5명씩
# 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때,
# 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# 마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.
def solution(names):
    answer = names[::5]
    return answer


# 할 일 목록
# 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
# todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(todo_list, finished):
    answer = []
    for i, s in enumerate(todo_list):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer


# n보다 커질 때까지 더하기
# 정수 배열 numbers와 정수 n이 매개변수로 주어집니다.
# numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            return answer
    return answer


# 수열과 구간 쿼리 1
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
def solution(arr, queries):
    for s, e in queries:
        for i in range(s,e+1):
            arr[i] += 1
    return arr







