def solution(number):
    answer = 0
    i = 0
    while i < len(number) :
        answer += int(number[i])
        i += 1
    return answer % 9