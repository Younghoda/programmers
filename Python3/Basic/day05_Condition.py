# 코드 처리하기
# 문자열 code가 주어집니다.
# code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.
# mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.
# mode가 0일 때
# code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
# mode가 1일 때
# code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
# 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.
# 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.
def solution(code):
    ret=''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 - mode
            continue
        if mode == 0:
            if code[idx] != 1:
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                mode =1
        if mode == 1:
            if code[idx] != 1:
                if idx%2 ==1:
                    ret += code[idx]
            else:
                mode =0
    if ret == '':
        ret = "EMPTY"
    return ret

# 다른 풀이
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'


# 등차수열의 특정한 항만 더하기
# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
# 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.
def solution(a, d, included):
    list = []
    answer = 0
    for i in range(len(included)):
        if included[i] == 1:
            list.append(a+i*d)
    for j in range(len(list)):
        answer += list[j]
    return answer


# 주사위 게임 2
# 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, c):
    if a == b and b == c:
        return (a+b+c) * (a**2 + b**2+ c**2) * (a**3 + b**3+ c**3)
    elif a != b and b != c and a != c:
        return a+b+c
    else:
        return (a+b+c) * (a**2 + b**2+ c**2)

# 다른 풀이
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)


# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer1 = 0
    answer2 = 1
    for i in num_list:
        answer1 += i
    for i in num_list:
        answer2 *= i
    if answer2 < answer1 **2:
        return 1
    else:
        return 0

# 다른 풀이(리스트의 합을 sum 함수를 이용해서 구할 수 있다.
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0


# 이어 붙인 수
# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    odd=''
    even=''
    for i in num_list:
        if i % 2 == 1:
            i = str(i)
            odd += i
        else:
            i = str(i)
            even += i
    return int(odd)+int(even)







