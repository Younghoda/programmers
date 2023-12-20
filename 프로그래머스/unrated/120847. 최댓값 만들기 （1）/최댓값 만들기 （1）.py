def solution(numbers):
    answer = 0
    a = max(numbers)
    print(a)
    numbers.remove(a)
    b = max(numbers)
    return a*b