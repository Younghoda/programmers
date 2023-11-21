########################################### 다시 풀어보기 ######################################
# 세 개의 구분자
# 임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.
# 예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.
# 문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.
def solution(myStr):
    answer = []
    s = myStr.replace('b','a')
    s = s.replace('c','a')
    s = s.split('a')
    s = [x for x in s if x != '']
    if not s:
        return ["EMPTY"]
    return s


# 배열의 원소만큼 추가하기
# 아무 원소도 들어있지 않은 빈 배열 X가 있습니다.
# 양의 정수 배열 arr가 매개변수로 주어질 때,
# arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer


# 빈 배열에 추가, 삭제하기
# 아무 원소도 들어있지 않은 빈 배열 X가 있습니다.
# 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고,
# flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.
def solution(arr, flag):
    answer = []
    for i, s in enumerate(arr):
        if flag[i]==True:
            for j in range(2*s):
                answer.append(s)
        else:
            answer = answer[:-s]
    return answer

# 또 다른 풀이(pop()함수를 이용)
def solution(arr, flag):
    X = []
    for i, f in enumerate(flag):
        if f:
            X += [arr[i]] * (arr[i]*2)
        else:
            for _ in range(arr[i]):
                X.pop()
    return X


# 배열 만들기 6
# 0과 1로만 이루어진 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk을 만드려고 합니다.
# i의 초기값을 0으로 설정하고 i가 arr의 길이보다 작으면 다음을 반복합니다.
# 만약 stk이 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
# stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거하고 i에 1을 더합니다.
# stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i]를 추가하고 i에 1을 더합니다.
# 위 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성해 주세요.
# 단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.
def solution(arr):
    answer = []
    i = 0
    while (i < len(arr)):
        if not answer:
            answer.append(arr[i])
            i += 1
        else:
            if answer[-1] == arr[i]:
                answer.pop()
                i += 1
            else:
                answer.append(arr[i])
                i += 1

    if not answer:
        return [-1]
    return answer





