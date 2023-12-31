#병든 나이트 (1시간 반 걸림 ㅅㅂ..;)
'''
문제
병든 나이트가 N x M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.

2칸 위로, 1칸 오른쪽
1칸 위로, 2칸 오른쪽
1칸 아래로, 2칸 오른쪽
2칸 아래로, 1칸 오른쪽
병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. 병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다. 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.

체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.

입력
첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어진다. N과 M은 2,000,000,000보다 작거나 같은 자연수이다.

출력
병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력한다.
'''
######idea######
# return : 방문할 수 있는 칸의 최대 개수
# 예제 1 1 -> 1을 보아 방문하는 칸 default 값은 1
# (방문하는 칸은 밟는 모든 타일이 아니라 최종적으로 찍는 타일을 말하며 이동 횟수와는 다른개념.)
# 방문하는 칸 수 = 1 + 이동횟수
# 세로의 크기 순서대로 하나씩 고려해본다.
# 조건을 고려하여 4개의 이동조건을 모두 사용할 때와 사용하지 않을 떄(않아도 될 때)를 생각해본다.

def sol(N,M):
    if N == 1 or M == 1:
        return 1
    
    if N == 2 :
        return min( 1 + (M-1)//2 , 4) # 1 + 이동 횟수 = 방문하는 칸 수. 즉 4는 3번 이동했다는 것.
    
    if N >= 3 and M >= 7: 
        return 1 + (4 + (M - 7)) # 네 조건이 모두 사용되는 경우의 최소 크기는 3x7. 이후 최대로 이동해야하기 떄문에 한칸씩 우측으로 가는 횟수 고려 (M-7)
    
    else : 
        return min (1 + (M-1), 4) # 3번까지 이동을 허용하여 오른쪽으로 1만큼 움직이는 횟수( 최대로 이동해야 하기 때문 : M-1)
    
N, M = map(int,input().split(' '))
print(sol(N, M))