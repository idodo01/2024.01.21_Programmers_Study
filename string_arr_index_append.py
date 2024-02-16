def solution(my_strings, parts):
    answer = ''

    for i in range(len(my_strings)) :
        index = parts[i][0]
        
        while index < parts[i][1]+1 :
            answer += my_strings[i][index]
            
            index += 1

    return answer
