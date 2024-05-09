def solution(n, slicer, num_list):
    answer = []
    
    # slicer = [a,b,c]
    # 0부터 b까지
    if n == 1 :
         for i in range(0,slicer[1]+1) :
                answer.append(num_list[i])
    # a부터 마지막까지
    elif n == 2 :
         for i in range(slicer[0],len(num_list)) :
                answer.append(num_list[i])
    # a부터 b까지
    elif n == 3 :
         for i in range(slicer[0],slicer[1]+1) :
                answer.append(num_list[i])
    # a부터 b까지, c간격으로
    elif n == 4 :
             for i in range(slicer[0],slicer[1]+1,slicer[2]) :
                answer.append(num_list[i])
    
    return answer
    