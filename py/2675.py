#각 테스트 케이스 별로 출력을 하니 오답이 되었다..
#테케를 모으고 테케별 출력을 하였다.
def out(r,s):
    for c in s:
        print(c*int(r), end='')
    
T = int(input())
t_list = []
for _ in range(T):
    t_list.append(input().split())
for test in t_list:
    out(test[0],test[1])
    print()
