def solution(arr):
    answer = []
    frist_index = 0
    last_index = 0
    
    if 2 in arr :
        # 첫번째 2 인덱스 구하기
        frist_index = arr.index(2)
        print(frist_index)
        
        # 마지막 2 인덱스 구하기
        for i in range(len(arr)) :
            if 2 == arr[i] :
                last_index = i
                print(last_index)
        
        # 2가 한 개 포함될 경우    
        if frist_index == last_index :
            answer.append(arr[frist_index])
        
        # 2가 여러개 포함될 경우
        else :
            for i in range(frist_index,last_index+1) :
                answer.append(arr[i])

    else :
        answer.append(-1)
        
        
    return answer