def solution(my_string, m, c):
    answer = ''
    str_inx = c-1
    
    for i in range(int(len(my_string)/m)):
        answer += my_string[str_inx]
        str_inx += m
    return answer
    
