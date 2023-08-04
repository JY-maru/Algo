#스텍 수열
#in
stack = []
result = []
n = int(input())
decide = True
cnt = 1
for _ in range(n):
    num = int(input())
    while cnt <= num: #cnt보다 큰 값일 때 해당 값까지 push
        result.append('+')
        stack.append(cnt)
        cnt += 1
    if stack[-1] == num : #오름차순 push를 감안하여 마지막 값이 같을때 pop
        stack.pop()
        result.append('-')
        
    else :  #마지막 값보다 더 작은 값이 들어있으므로 해당 조건 시 num을 찾을 수 없다. false로 판단 가능
        decide = False
        print('NO')
        break

if decide:
    for elem in result:
        print(elem)

