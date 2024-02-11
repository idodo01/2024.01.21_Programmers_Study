def solution(my_string, index_list):
    answer = ''
    i,j = 0, 0
    while i < len(my_string) :
        
        while j < len(index_list) :
            answer += my_string[index_list[j]]
            j+=1
        
        i += 1
        
    return answer