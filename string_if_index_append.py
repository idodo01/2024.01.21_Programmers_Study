def solution(intStrs, k, s, l):
    answer = []
    num = '' # intStrs에서 s부터 l길이 만큼 떼온 string
    
    for i in range(len(intStrs)) :
        index = s
        num = ''
        
        for j in range(l) :
            num += intStrs[i][index]
            
            index += 1
        if int(num) > k :
            answer.append(int(num))

    return answer
    
print(solution(["0123456789","9876543210","9999999999999"],50000, 5, 5))