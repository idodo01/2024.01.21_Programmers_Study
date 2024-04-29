def solution(arr, idx):
    answer = ''
    check_index = False
    values_index = 0
    
    for i in range(len(arr)) :
        if i > idx and arr[i] == 1 :
            check_index = True
            values_index = i
    
    if check_index == True :
        return values_index
    else :
        return -1
        
              
# 해당 문제 오류
''' arr	idx	result
[0, 0, 0, 1]	        1	    3 
[1, 0, 0, 1, 0, 0]	    4	    -1
[1, 1, 1, 1, 0]	        3	    3

3번째 입출력 예시가
문제에서 제시한 'idx보다 크면서' 
조건에 맞지않는 결과값을 낸다

'idx보다 크거나 같다'가 되어야 3이 나온다.
            
            