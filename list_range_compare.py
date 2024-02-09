def solution(arr, queries):
    answer = []
    big_value = []
    
    result_value = 0
    
    i = 0 # queries의 인덱스
    j = 0 # s부터 e까지
    
    while i < len(queries) :
        # [s, e, k], [s, e, k], [s, e, k]
        j = queries[i][0] # s부터 
        while j < queries[i][1]+1 : #e까지
            
            # 모든 arr[j]가 k보다 크면서
            # 가장 작은 arr[j] 찾기
            if arr[j] > queries[i][2] : # k
                big_value.append(arr[j]) # k보다 큰 arr[j]들
                # print('{}가{}보다 크다'.format(arr[j],queries[i][2]))
            j += 1
        
        # k보다 큰 값이 없다
        if len(big_value) == 0 :
            result_value = -1
        else : # k보다 큰 arr[j]들중에서 가장 작은 값구하기
            result_value = min(big_value)
        # print(big_value)
        # print('{}의 result는 {}'.format(i,result_value))   
        answer.append(result_value)
        
        big_value = [] # # k보다 큰 arr[j]들 리스트 - 초기화
        i += 1
        
    return answer
    

        