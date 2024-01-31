def solution(num_list):
    answer = 0
    
    multiply_num = 1 # 모든 원소들의 곱
    
    sum_num = 0 # 모든 원소들의 합
    sum_double_num = 0 # 모든 원소들의 합의 제곱
    
    i = 0
    
    while i < len(num_list) : 
        # 모든 원소들의 곱 구하기
        multiply_num *= num_list[i]
        # 모든 원소들의 합 구하기
        sum_num += num_list[i]
        
        i += 1
       

    # 모든 원소들의 합의 제곱과 비교하기
    sum_double_num = sum_num*sum_num    
    
    if multiply_num < sum_double_num :
        answer = 1
    elif multiply_num > sum_double_num :
        answer = 0
        
    return answer