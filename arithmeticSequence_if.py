def solution(a, d, included):
    answer = 0
    
    i = 0
    sum = a 
    
    while i < len(included) :
        
        if included[i] == True :
            answer += sum
            
        sum += d
        i += 1
    
    return answer
    
    
    
    
