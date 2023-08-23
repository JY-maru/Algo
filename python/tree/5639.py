# 이진검색트리 
'''
문제
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다. 후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다. 예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

입력
트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

출력
입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.
'''
''' 시간초과 : O(NlogN)
## method
class Node:
    def __init__(self,items, left, right) -> None:
        self.data = items
        self.left = left
        self.right = right  

class BST:
    def __init__(self):
        self.__root = None
    
    def insert(self, items):
        # root부터 삽입
        self.__root = self.__insertItem(self.__root,items)

    def __insertItem(self, tNode : Node, items) -> Node:
        if tNode == None: # 노드 없을 때 새로 생성
            tNode = Node(items, None, None)
        
        elif tNode.data > items:
            tNode.left = self.__insertItem(tNode.left, items)
        
        else :
            tNode.right = self.__insertItem(tNode.right, items)

        return tNode
    
    def postorder(self):
        self.__postorder_Recu(self.__root)

    def __postorder_Recu(self, curNode):
        if curNode != None:
            self.__postorder_Recu(curNode.left)
            self.__postorder_Recu(curNode.right)
            print(curNode.data)
    def root(self):
        return self.__root.data
## input
import sys
sys.setrecursionlimit(10**4)
tr = BST()
while 1:
    try : 
        tr.insert(int(sys.stdin.readline()))
    except: break
## output
tr.postorder()
print(tr.root())
'''

# -> 입력이 들어오면 트리를 생성하지 않고 바로 후위 순회식 출력
# root보다 큰 수가 나오는 구간부터 오른쪽 서브트리므로 자름.
## method
def postorder(start, end):
    if start > end :
        return
    
    div = end+1
    for i in range(start+1, end+1):
        if preorder[start] < preorder[i] : # 왼쪽 서브트리 발견
            div = i
            break

    root = start
    postorder(root+1, div-1) # 왼쪽 서브트리
    postorder(div, end) # 오른쪽 서브트리 
    print(preorder[root])
## input
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
preorder = []
while 1:
    try : 
        preorder.append(int(input()))
    except: break

## output
postorder(0,len(preorder)-1)