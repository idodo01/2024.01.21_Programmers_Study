def solution(a, b):
    answer = 0
    
    # 값 붙이기
    attach_ab = int(str(a)+str(b))
    attach_ba = int(str(b)+str(a))
    
    # 값 비교하기
    if attach_ab >= attach_ba:
        answer = attach_ab
    else :
        answer = attach_ba

    return answer
    
print(solution(89,8))