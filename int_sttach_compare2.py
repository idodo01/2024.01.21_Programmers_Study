def solution(a, b):
    answer = 0
    
    # 값 붙이기
    attach_ab = int(str(a)+str(b))
    attach_2ab = 2*a*b 
    
    # 값 비교하기
    if attach_ab >= attach_2ab:
        answer = attach_ab
    else :
        answer = attach_2ab

    return answer

print(solution(89,8))