# N-Queen
'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''
## method
def sol(k): # k : 놓은 말 개수 - 점유 행 번호로도 활용 가능
    # 퀸 : 상하좌우 - x, y 좌표 확인 / 대각선 - (y=x 선상 : used_up) x-y 같으면. (y=-x 선상 : used_down) x+y같으면 놓을 수 없음.
    global n, cnt
    
    if k == n :
        cnt += 1
        return

    # i : 점유 열 번호로 활용 가능
    for i in range(n):
        if not used_c[i] and not used_up[k+i] and not used_down[(n-1)+k-i]:
            used_c[i] = True
            used_up[k+i] = True
            used_down[(n-1)+k-i] = True
            sol(k+1)
            used_c[i] = False
            used_up[k+i] = False
            used_down[(n-1)+k-i] = False


## input
n = int(input())
maps = [[0]*n for _ in range(n)]
# 열 점유 여부
used_c = [False]*n
# y=x 선상
used_up = [False]*(2*(n-1)+1)
#y=-x 선상
used_down = [False]*(2*(n-1)+1)

cnt = 0

## output
sol(0)
print(cnt)

