def solution(numbers, k):
    answer = 0
    arr = []
    for i in range(k):
        arr += numbers
    return arr[2*(k-1)]