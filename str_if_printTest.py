def solution(code):
    answer = ''
    
    mode = 0 # mode는 시작할 때 0
    ret = ''
    
    idx = 0
    
    for i in code :

        # mode가 0일 때
        # code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
        # code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
        
        if mode == 0 :
            if code[idx] != '1' :
                if idx % 2 == 0 :
                    ret += code[idx]
            elif code[idx] == '1' :
                mode = 1
                
        # mode가 1일 때
        # code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
        # code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.        
        elif mode == 1 : 
            if code[idx] != '1' :
                if idx % 2 == 1 :
                    ret += code[idx]
            elif code[idx] == '1' :
                mode = 0
                
        idx += 1
    
    # return 하려는 ret가 만약 빈 문자열이라면 
    # 대신 "EMPTY"를 return 합니다.
    if ret == '' :
        answer = 'EMPTY'
    else :
        answer = ret
        
    return answer
   