def str_test(str1, str2):
    answer = ''
    
    str_len = len(str1)+len(str2)
    
    i = 0
    str1_index = 0
    str2_index = 0
    
    while i < str_len:
        if i % 2 == 0 :
            answer += str1[str1_index]
            str1_index += 1
        else :
            answer += str2[str2_index]
            str2_index += 1
        i += 1
            
    return answer
    
print(str_test("aaaaa","bbbbb"))