#필란드롬 판단하기
def sol(n):
    for i in range(len(n)):
        if n[i] != n[-(i+1)]:
            return 'no'
    return 'yes'


#in
inlist = []
while 1 :
    n = input()
    if n == '0':
        break
    inlist.append(n)

    #out
    print(sol(n))
