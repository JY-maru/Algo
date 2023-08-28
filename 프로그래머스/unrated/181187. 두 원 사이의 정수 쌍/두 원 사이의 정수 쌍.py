def count_spot(r): #크기 r인 원 안의 점을 세는 함수
    y = r
    cnt = 0
    line_spot = 0 # 선 위의 점 카운트
    for x in range(r+1):
        if x**2 + y**2 > r**2 :
            while 1:
                y -= 1
                if x**2 + y**2 <= r**2:
                    if x**2 + y**2 == r**2:
                        line_spot += 1
                    break
        elif x**2 + y**2 == r**2:
            line_spot += 1
            
        cnt += y+1 # 0인 지점도 세어야 함.
        
    return 4*(cnt-r-1) +1 , 4*(line_spot-1)

def solution(r1, r2):
    cnt1, line1 = count_spot(r1)
    cnt2, line2 = count_spot(r2)
    
    return cnt2-cnt1 + line1# 최소원이 축과 만나는 부분까지 삭제되므로 만나는 부분 더함