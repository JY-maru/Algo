def solution(scores):
    answer = 1
    pa, pb = scores[0]
    tscore = pa+pb
    # 나중에 나온 원소의 두번째 elem이 지금껏 나온 두번째 elem중 가장 작으면 인사고과 배제 가능
    scores = sorted(scores, key = lambda x : (-x[0], x[1]))
    maxb = 0
    
    for a,b in scores:
        # 한명이라도 적은경우 
        if pa < a and pb < b : return -1
        
        # 기존보다 크다면
        if b >= maxb : 
            maxb = b
            
            
            if tscore < a+b :
                
                answer += 1
    
    return answer
    