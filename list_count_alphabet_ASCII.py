def solution(my_string):
    answer = [0]*52
    count = 0
    
    for i in my_string :

        # 아스키 코드 65 ~ 90 => 'A'~'Z'
        for j in range(0,26) :
            if(i==chr(j+65)) :
                answer[j]+=1
        # 아스키 코드 97 ~ 122 => 'a'~'z'       
        for j in range(26,52) :
            if(i==chr(j+71)) :
                answer[j]+=1

    
    return answer
    