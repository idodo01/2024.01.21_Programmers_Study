def solution(n):
    answer = 0
    
    # n이 홀수
    if n % 2 == 1 :
        while n != 0 :
            # n 이하의 홀수인 모든 양의 정수의 합 구하기
            if n % 2 == 1 :
                answer += n
            n -= 1
        return answer
    
    # n이 짝수
    else : 
        while n != 0 :
            # n 이하의 짝수인 모든 양의 정수의 제곱의 합 구하기
            if n % 2 == 0 :
                answer += n * n
            n -= 1    
        return answer