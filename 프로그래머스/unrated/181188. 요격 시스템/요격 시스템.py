def solution(targets):
    sorted_t = list(sorted(targets,key = lambda x : x[1]))
    
    answer = 1
    y = sorted_t[0][1]
    
    for s,e in sorted_t:
        if s < y <= e: continue
        else : 
            y = e
            answer += 1
    
    return answer
   