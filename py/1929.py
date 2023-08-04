# n~m까지 존재하는 소수 출력하기.

def prime(n,m):
    table = [1 if (x >= 2) else 0 for x in range(0, m+1)]
    
    for piv in range(2, m+1):
        for div in range(2,int(m/piv)+1):
            if table[piv*div] == 1:
                table[piv*div] = 0
    
    for idx in range(n, len(table)):
        if table[idx] == 1:
            print(idx)
#in
n,m = map(int,input().split())

#out
if m == 1 :
    print(0)
else :
    prime(n,m)