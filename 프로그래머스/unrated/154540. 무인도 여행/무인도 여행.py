def bfs(maps, visited, s): # s: (r,c)
    from collections import deque
    will_visit = deque([s])
    r = (1,-1,0,0)
    c = (0,0,1,-1)
    R,C = len(maps), len(maps[0])
    total = []
    
    while will_visit:
        vr,vc = will_visit.popleft()
        if (vr,vc) in visited : continue
        visited.add((vr,vc))
    
        total.append(int(maps[vr][vc]))
        
        for dr, dc in list(zip(r,c)):
            nr, nc = vr+dr, vc+dc
            
            if 0<=nr<R and 0<=nc<C :
                if maps[nr][nc] == 'X': continue
                if (nr,nc) not in visited:
                    will_visit.append((nr,nc))
    return sum(total)
    
def solution(maps):
    answer = []
    visited = set()
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'X' or (r,c) in visited: continue
            answer.append(bfs(maps,visited, (r,c)))
            
    if answer == []: answer.append(-1)
    return sorted(answer)