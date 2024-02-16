def solution(my_string):
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
    
    answer.sort()
    return answer