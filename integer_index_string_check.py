def solution(l, r):
    answer = []
    
    i = l
    i_str = ''  # i 정수의 구성을 인덱스로 확인하기 위해서 
                # string 변환시 사용될 변수
    j = 0
    num_check = False # "5" 또는 "0"이외의 숫자가 포함된 정수일 경우 true
    
    while i < r+1 :
        #print("{}숫자".format(i))

        i_str = str(i)
        #print(j,len(i_str))
        
        while j < len(i_str) : 
            # "5" 또는 "0" 이외의 숫자가 포함된 정수일 경우
            if i_str[j] != '5' and i_str[j] != '0' :
                num_check = True
                
            # print("{}숫자의 {}번째 수 체크: {}, {}".format(i,j,i_str[j],num_check))
            j += 1
            
        # "5" 또는 "0"만 포함된 정수일 때
        # 배열에 저장됨
        
        # i 정수를 string으로 변환했던 i_str 변수를 
        # integer로 변환해서 삽입
        if num_check == False :
            answer.append(int(i_str))
        
        #print(answer)
        
        num_check = False
        i += 1
        j = 0 
        
    if len(answer) == 0 :
        answer.append(-1)
    
    return answer
    
#solution(5,555)