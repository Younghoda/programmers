# 뒤에서 5등 위로
# 정수로 이루어진 리스트 num_list가 주어집니다.
# num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    num_list.sort()
    return num_list[5:]


# 전국 대회 선발 고사
# 0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다.
# 등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.
# 각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다.
# 전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.
def solution(rank, attendance):
    arr=[]
    for i, s in enumerate(attendance):
        if s == True:
            arr.append(rank[i])
    arr.sort()
    a1,b1,c1 = arr[:3]
    for i,s in enumerate(rank):
        if s==a1:
            a = i
        elif s==b1:
            b=i
        elif s==c1:
            c=i
    return 10000*a+100*b+c


# 정수 부분
# 실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.
def solution(flo):
    return int(flo)


# 문자열 정수의 합
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer


# 문자열을 정수로 변환하기
# 숫자로만 이루어진 문자열 n_str이 주어질 때, n_str을 정수로 변환하여 return하도록 solution 함수를 완성해주세요.
def solution(n_str):
    return int(n_str)







