def solution(my_string, is_prefix):
    answer = []
    str = ''
    i = 1

    while i < len(my_string)+1 :
        str = ''
        j = 0
        while j < i :
            str += my_string[j]
            j += 1
        answer.append(str)
        i += 1
    
    if is_prefix in answer :
        return 1
    else :
        return 0

solution("banana"	,"ban")