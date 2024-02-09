def solution(arr, queries):
    answer = []
    temp = 0

    
    i = 0
    while i < len(queries) :
        temp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = temp
        i += 1
    answer = arr    
    return answer