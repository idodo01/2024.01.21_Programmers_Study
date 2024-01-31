def solution(num_list):
    answer = 0
    
    # 홀수만 순서대로 이어붙인 string
    odd_num_str = ''
    # 짝수만 순서대로 이어붙인 string
    even_num_str = ''
    
    
    i = 0
    while i < len(num_list) :
        if num_list[i] % 2 == 1 :
            odd_num_str += str(num_list[i])
        else :
            even_num_str += str(num_list[i])
        i += 1
        
    answer = int(odd_num_str) + int (even_num_str)
    
    return answer