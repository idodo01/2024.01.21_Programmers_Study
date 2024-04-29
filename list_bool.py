def solution(my_string, indices):
    answer = ''
    check = True
    
    
    for i in range(len(my_string)) :
        for j in range(len(indices)):
            if i == indices[j] :
                 check = False
                 
        if(check) :
            answer += my_string[i]
        check = True

    return answer
    