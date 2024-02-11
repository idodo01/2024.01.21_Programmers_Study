def solution(my_string, queries):
    answer = ''
    reverse_string = ''
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    
    while i < len(queries) :
         
        answer = ''
        
        j = queries[i][0]
        # 뒤집어야 하는 index 전까지의 string을 answer변수에 미리 담는다
        while k < j :
            answer += my_string[k]
            k += 1
        # 뒤집어야하는 string을 reverse_string 변수에 담는다
        while j < queries[i][1]+1 :
            reverse_string += my_string[j]
            j += 1
        # reverse_string 변수에 담긴 string을 뒤집어 answer변수에 담는다
        answer += reverse_string[::-1]
        # queries[i][1]+1 인덱스부터의 string를 뒤에 이어서 담는다  
        m = queries[i][1]+1
        while m < len(my_string) :
            answer += my_string[m]
            m += 1
        
        k = 0
        reverse_string = ''
        my_string = answer
        
        i += 1
        
    return answer
    
solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]])