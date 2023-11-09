# # 정수 찾기
# # 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.
# def solution(num_list, n):
#     for i in num_list:
#         if i == n:
#             answer = 1
#             break
#         else:
#             answer = 0
#     return answer



# # flag에 따라 다른 값 반환하기
# # 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
#
# def solution(a, b, flag):
#     if flag:
#         answer = a + b
#     else:
#         answer = a-b
#     return answer



# # 이어 붙인 수
# # 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
# def solution(num_list):
#     odd=''
#     even=''
#     for i in num_list:
#         if i % 2 == 1:
#             i = str(i)
#             odd += i
#         else:
#             i = str(i)
#             even += i
#     return int(odd)+int(even)










