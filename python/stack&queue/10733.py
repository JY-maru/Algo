#제로합
#0일때 최근에 들어온 수를 지우고, 아닐 경우는 입력된 수를 데이터에 추가한다.
#자료구조 : deque (delete/insert를 O(1)로 용이하게 하기 위함)

def deque_sum(num):
    from collections import deque
    
    dlist = deque([])
    for _ in range(num):
        elem = int(input())
        if elem != 0 :
            dlist.appendleft(elem)
        else :
            dlist.popleft()
    
    return sum(dlist)


num = int(input())
print(deque_sum(num))
