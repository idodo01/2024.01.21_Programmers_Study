def solution(n, k):
    answer = []
    count = 1
    while k*count <= n :
        answer.append(k*count);
        count += 1
    
    return answer