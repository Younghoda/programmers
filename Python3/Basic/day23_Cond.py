# 부분 문자열
# 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
# 문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(str1, str2):
    return int(str1 in str2)


# 꼬리 문자열
# 문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다.
# 예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.
# 문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if not(ex in i):
            answer+=i
    return answer


# 정수 찾기
# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    for i in num_list:
        if i == n:
            return 1
        else:
            answer = 0
    return 0


# 주사위 게임 1(절대값 함수 abs()사용)
# 1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.
# a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
# a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
# a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
# 두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b):
    answer = 0
    if a%2 ==1 and b%2 ==1:
        return a**2 +b**2
    elif a%2 ==0 and b%2 ==0:
        return abs(a-b)
    else:
        return 2*(a+b)


# 날짜 비교하기
# 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
# 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.
def solution(date1, date2):
    answer = 0
    if date1[0] < date2[0]:
        return 1
    elif date1[0] > date2[0]:
        return 0
    if date1[1] < date2[1]:
        return 1
    elif date1[1] > date2[1]:
        return 0
    if date1[2] < date2[2]:
        return 1
    return answer

# 다른 풀이(리스트도 부등호 사용 가능!)
def solution(date1, date2):
    return int(date1 < date2)





