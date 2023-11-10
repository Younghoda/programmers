# n의 배수
# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num, n):
    if num%n ==0:
        return 1
    else:
        return 0


# 공배수
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(number, n, m):
    if number%n == 0 and number%m ==0:
        return 1
    else:
        return 0

# 다른 풀이
def solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))


# 홀짝에 따라 다른 값 반환하기
# 양의 정수 n이 매개변수로 주어질 때,
# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
def solution(n):
    answer = 0
    if n%2 == 1:
        for i in range(1,n+1):
            if i%2 == 1:
                answer += i
    else:
        for i in range(1,n+1):
            if i%2 == 0:
                answer += i*i
    return answer

# 다른 풀이
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


# 조건 문자열
# 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
# 두 수가 n과 m이라면
# ">", "=" : n >= m
# "<", "=" : n <= m
# ">", "!" : n > m
# "<", "!" : n < m
# 두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다.
# 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.
def solution(ineq, eq, n, m):
    if (ineq == '>' and eq == '='):
        if n >= m:
            return 1
        else:
            return 0
    elif (ineq == '<' and eq == '='):
        if n <= m:
            return 1
        else:
            return 0
    elif (ineq == '>' and eq == '!'):
        if n > m:
            return 1
        else:
            return 0
    elif (ineq == '<' and eq == '!'):
        if n < m:
            return 1
        else:
            return 0

# 다른 풀이
def solution(ineq, eq, n, m):
    return int(bool(str(n)+ineq+eq.replace('!', '')+str(m)))


# flag에 따라 다른 값 반환하기
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, flag):
    if flag:
        answer = a + b
    else:
        answer = a-b
    return answer

