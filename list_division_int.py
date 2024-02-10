def solution(n):
    answer = []
    
    answer.append(n)
    
    while n != 1 :
        print(n)
        # n이 짝수일 때
        if n % 2 == 0 :
            n /= 2
            print(n)
        else :
            n = 3 * n + 1
            print(n)
        answer.append(int(n))
    return answer
