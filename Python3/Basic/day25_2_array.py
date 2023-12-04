########################################### 다시 풀어보기 ######################################
# 정수를 나선형으로 배치하기
# 양의 정수 n이 매개변수로 주어집니다.
# n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.


# 특별한 이차원 배열 2
# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
# 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(i+1):
            if i != j:
                if arr[i][j] != arr[j][i]:
                    answer = 0
    return answer


# 정사각형으로 만들기
# 이차원 정수 배열 arr이 매개변수로 주어집니다.
# arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고,
# 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    arr1 = []

    for i in range(len(arr)):
        arr1.append(len(arr[i]))

    col = max(arr1)
    row = len(arr)
    arr2 = [0] * col

    if col > row:
        for i in range(col - row):
            arr.append(arr2)

    elif row > col:
        for i in range(row):
            for j in range(row - col):
                arr[i].append(0)
    return arr


# 이차원 배열 대각선 순회하기
# 2차원 정수 배열 board와 정수 k가 주어집니다.
# i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요.
def solution(board, k):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]

    return answer



