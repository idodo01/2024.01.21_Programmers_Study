def solution(my_string, is_suffix):
    answer = []
    str = ''
    j = 0
    k = 0
    
    for i in range(len(my_string)) :
        str = ''
        while j < len(my_string) :
            str += my_string[j]
            j += 1
        k += 1
        j = k
        answer.append(str)
    
    if is_suffix in answer :
        return 1
    else :
        return 0

