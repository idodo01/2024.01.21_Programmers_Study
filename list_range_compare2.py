def solution(arr, queries):
    answer = []
    
    i = 0 # queries의 인덱스
    j = 0 # s부터 e까지
    
    while i < len(queries) :
        # [s, e, k], [s, e, k], [s, e, k]
        j = queries[i][0] # s부터 
        while j < queries[i][1]+1 : #e까지
            
            if j % queries[i][2] == 0 : # j가 k의 배수이면
                arr[j] += 1
            j += 1
        
        i += 1
        
        
    return arr
    

        