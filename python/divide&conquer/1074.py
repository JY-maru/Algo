'''
문제
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2**(N-1) × 2**(N-1)로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 2**2 × 2**2 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.

입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.
'''

# 전체 2**n 크기 사각형을 2**(n-1)의 범위로 쪼개어 해당 범위에 들어오면 축소하여 생각한다.


## method
def sol(N,r,c):
    answer = 0

    for n in range(N-1, -1, -1):
        start = [(0,0),(0,2**(n)),(2**(n),0),(2**n,2**n)]
        end = [(r+2**n,c+2**n) for r,c in start]
        cnt = 0
        
        for s,e in zip(start,end):
            sr,sc = s ; er,ec = e
            
            if sr <= r < er and sc <= c < ec:
                answer += cnt*(2**(2*n)) # 사각형의 넓이만큼 곱하면 앞에 굳이 세지 않아도 됨.
                break
            cnt += 1
        r %= 2**n
        c %= 2**n
    return answer
    
## input
N, r, c = map(int,input().split())
## output
print(sol(N,r,c))