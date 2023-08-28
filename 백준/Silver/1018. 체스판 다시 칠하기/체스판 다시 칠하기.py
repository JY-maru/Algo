## method
def sol(n,m):
    c1, c2 = float('inf'), float('inf')
    
    for r in range(n-7):
        for c in range(m-7):
            # print(r,c)
            chess_board = [board[i][c : c+8] for i in range(r,r+8)]
            # print(chess_board)
            tmp1, tmp2 = get_color(chess_board) 
            # print(tmp1,tmp2)
            c1, c2 = min(c1,tmp1), min(c2,tmp2)
    return min(c1,c2)

def get_color(chessBoard) -> tuple: 
    c1, c2 = 0,0

    for r in range(8):
        for c in range(8):
            # WB로 시작
            if ((r+c) % 2 == 0 and chessBoard[r][c] != 'W') or ((r+c) % 2 == 1 and chessBoard[r][c] != 'B'):
                c1 += 1

            # BW로 시작
            elif ((r+c) % 2 == 0 and chessBoard[r][c] != 'B') or ((r+c) % 2 == 1 and chessBoard[r][c] != 'W'):
                c2 += 1
        
    return c1,c2

## input
N,M = map(int,input().split())
board = [input() for _ in range(N)]

## output
print(sol(N,M))