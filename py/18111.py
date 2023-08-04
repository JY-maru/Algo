#마인크래프트
#자료구조 : counter(dict형태)
#생각해보니, 제시된 블록에서 쌓아올리는 것 물론 제시 되지 않은 높이에서 최적해가 나올 수 있다.

def sol(b):
    keys = sorted(list(cnt.keys()))
    init_b = b #초기 블록값
    t, need = 0, 0 #소요시간, 평탄화에 필요한 블록값
    leng = len(keys)
    result = []

    for pidx in range(leng):
        pivot = keys[pidx] #기준 높이
        for i in range(pidx+1,leng):
            need += cnt[keys[i]]
            t += need * 2
            b += need
        need = 0

        for j in range(pidx):
            need += cnt[keys[j]]
            t += need
        
        if b - need < 0:
            continue
        result.append((t, pivot))
        t, need, b = 0, 0, init_b
    
    result = sorted(result, key = lambda x : x[1], reverse = True)
    result = sorted(result, key= lambda x : x[0])

         
    return result[0][0], result[0][1]


#in 
import sys
from collections import Counter
n,m,b = map(int, input().split())
cnt = Counter()
for _ in range(n):
    cnt += Counter(list(map(int,sys.stdin.readline().split())))

#out
print(sol(b)[0],sol(b)[1])