def solution(sequence, k):
    answer = []
    seq = sorted(sequence)
    n = len(seq)
    total = last = 0
    
    for front in range(n):
        
        while total < k and last < n:
            total += seq[last]
            last += 1
            
        if total == k : 
            answer.append([last-front, front, last-1])
        total -= seq[front]
    
    return sorted(answer)[0][1:]
