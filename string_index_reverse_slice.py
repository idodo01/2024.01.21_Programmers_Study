def solution(my_string, s, e):
    answer = ''
    string = ''
    
    # 1. 뒤집을 문자열 앞까지 
    answer += my_string[0:s]

    # 2. slice를 이용하여 문자열 뒤집기
    # [start:stop:step] 의미
    i = s
    while i < e+1 :
        string += my_string[i] 
        i += 1
    answer += string[::-1] 
    
    # 3. 뒷부분 뒤집기
    answer += my_string[e+1:len(my_string)]

        
    return answer
    
solution("Progra21Sremm3",	6,	12)