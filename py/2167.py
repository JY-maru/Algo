#알고리즘 : dp
#이전의 합을 기록하여 열별로 값을 재할당. 윗 열의 합은 다음 열 합들에 포함되어 있지 않음.

def sum(list,i,j,x,y,l,r):
    sum = 0
    for idx in range(i,x+1):
        sum += dp[idx][y] - dp[idx][j-1] 
    return sum

l , r = map(int, input().split())
arr_2 = []
for _ in range(l):
    arr_2.append(list(map(int,input().split())))

dp = [[0]*(r+1) for _ in range(l+1)]

for low_idx in range(1,len(arr_2)+1):
    for col_idx in range(1,len(arr_2[0])+1):
        if col_idx == 1:  
            dp[low_idx][col_idx] += arr_2[low_idx-1][col_idx-1]
        else:
            dp[low_idx][col_idx] += dp[low_idx][col_idx-1]+arr_2[low_idx-1][col_idx-1]
for _ in range(int(input())):
    i,j,x,y = map(int, input().split())
    print(sum(dp,i,j,x,y,l,r))
    