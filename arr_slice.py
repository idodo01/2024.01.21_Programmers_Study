def solution(arr, query):
    for i in range(len(query)) :
        # 짝수이면 뒷부분을 자른다 -> 0 인덱스부터 해당 인덱스까지 
        if i % 2 == 0 :
            arr = arr[:query[i]+1]
            
        # 홀수이면 앞부분을 자른다 -> 해당 인덱스부터 끝까지
        else :
            arr = arr[query[i]:]
    return arr