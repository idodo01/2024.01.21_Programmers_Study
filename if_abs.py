def solution(a, b, c, d):
    answer = 0
    
    # 네 주사위에서 나온 숫자가 모두 p로 같다면
    if (a == b) and (a == c) and (a == d) and (b == c) and (b == d) and (c == d):
        answer = 1111 * a
    # 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면
    # a, b, c 가 같고 d 만 다르다
    elif ((a == b) and (a == c) and (b == c) and (a != d)) :
        answer = (10 * a + d) ** 2
    # a, b, d 가 같고 c 만 다르다
    elif ((a == b) and (a == d) and (b == d) and (a != c)) :
        answer = (10 * a + c) ** 2
    # a, c, d 가 같고 b 만 다르다
    elif ((a == c) and (a == d) and (c == d) and (a != b)) :
        answer = (10 * a + b) ** 2
    # b, c, d 가 같고 a 만 다르다
    elif ((b == c) and (b == d) and (c == d) and (b != a)) :
        answer = (10 * b + a) ** 2
        
     
    # a, b 가 같다
    elif (a == b) and (a != c) and (a != d) :
        # c, d가 같을 때
        if c == d :
            answer = (a + c) * abs(a - c)   # abs() : 절댓값
        # c, d가 다를 때
        else :
            answer = c * d
    # a, c 가 같다
    elif (a == c) and (a != b) and (a != d) :
        # b, d가 같을 때
        if b == d :
            answer = (a + b) * abs(a - b) 
        # b, d가 다를 때
        else :
            answer = b * d
    # a, d 가 같다
    elif (a == d) and (a != b) and (a != c) :
        # b, c가 같을 때
        if b == c :
            answer = (a + b) * abs(a - b) 
        # b, c가 다를 때
        else :
            answer = b * c        
    # b, c 가 같다
    elif (b == c) and (b != a) and (b != d) :
        # a, d가 같을 때
        if a == d :
            answer = (a + b) * abs(a - b)  
        # a, d가 다를 때
        else :
            answer = a * d
    # b, d 가 같다
    elif (b == d) and (b != a) and (b != c) :
        # a, c가 같을 때
        if a == c :
            answer = (a + b) * abs(a - b)  
        # a, c가 다를 때
        else :
            answer = a * c
    # c, d 가 같다
    elif (c == d) and (c != a) and (c != b) :
        # a, b가 같을 때
        if a == b :
            answer = (a + c) * abs(a - c)  
        # a, b가 다를 때
        else :
            answer = a * b
        
    # 네 주사위에 적힌 숫자가 모두 다르다면    
    elif (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d) :
        answer = [a,b,c,d]
        answer = min(answer)
        
    
    return answer
