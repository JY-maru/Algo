#구현(implement)
def sol(put,m):
    rank = sorted(list(set(put)),reverse = True)
    if len(rank) == len(put):
        return rank.index(put[m])+1
    
    data = []
    
    target = m 
    answer = 0 #count output

    while(1):
        if rank[0] != put[0] :
            put.append(put.pop(0)) #뒤로 빼기
            if target == 0:
                target += len(put)-1
                continue
            target -= 1
            
        else :
            put.pop(0)
            answer += 1
            if target == 0:
                return answer 
            target -= 1
            if rank[0] in put :
                continue
            else :
                rank.pop(0)
            
#in
N = int(input())
for _ in range(N):
    leng, m = map(int, input().split())
    put = list(map(int,input().split()))
    print(sol(put,m))