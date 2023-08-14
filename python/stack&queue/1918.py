'''
문제
수식은 일반적으로 3가지 표기법으로 표현할 수 있다. 연산자가 피연산자 가운데 위치하는 중위 표기법(일반적으로 우리가 쓰는 방법이다), 연산자가 피연산자 앞에 위치하는 전위 표기법(prefix notation), 연산자가 피연산자 뒤에 위치하는 후위 표기법(postfix notation)이 그것이다. 예를 들어 중위 표기법으로 표현된 a+b는 전위 표기법으로는 +ab이고, 후위 표기법으로는 ab+가 된다.

이 문제에서 우리가 다룰 표기법은 후위 표기법이다. 후위 표기법은 위에서 말한 법과 같이 연산자가 피연산자 뒤에 위치하는 방법이다.
이 방법의 장점은 다음과 같다. 우리가 흔히 쓰는 중위 표기식 같은 경우에는 덧셈과 곱셈의 우선순위에 차이가 있어 왼쪽부터 차례로 계산할 수 없지만 
후위 표기식을 사용하면 순서를 적절히 조절하여 순서를 정해줄 수 있다. 
또한 같은 방법으로 괄호 등도 필요 없게 된다. 예를 들어 a+b*c를 후위 표기식으로 바꾸면 abc*+가 된다.

중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다. 우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다. 
그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다. 그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다. 마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

다른 예를 들어 그림으로 표현하면 A+B*C-D/E를 완전하게 괄호로 묶고 연산자를 이동시킬 장소를 표시하면 다음과 같이 된다.



결과: ABC*+DE/-

이러한 사실을 알고 중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오

입력
첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다. 
그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다. 표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 
길이는 100을 넘지 않는다. 

출력
첫째 줄에 후위 표기식으로 바뀐 식을 출력하시오
'''
# 우선순위 높은 식 내 존재하는 부호를 stack에 넣는다.

## method
def sol(expr):
    leng = len(expr)
    oper_stack = []
    answer = ''

    for i in range(leng):
        if expr[i].isalpha(): answer += expr[i]
        else : # expr[i] 가 +,-,*,/,(,)
            if expr[i] == '(': oper_stack.append(expr[i])
            elif expr[i] in ('*','/'): # stack top이 + - 이면 추가할 수 있음 * / 이면(우선 순위 같으면) 뺴내야 함.
                while oper_stack and oper_stack[-1] in ('*','/'):
                    answer += oper_stack.pop()
                oper_stack.append(expr[i])
            elif expr[i] in ('+','-'): # 스텍 내 연산자들보다 우선순위가 무조건 같거나 작기 때문에 무조건 뺴낼 예정
                while oper_stack and oper_stack[-1] != '(': #스텍 내 연산자들을 다 빼내야함. ( 존재한다면 ( 전까지
                    answer += oper_stack.pop()
                oper_stack.append(expr[i])
            elif expr[i] == ')':
                while oper_stack and oper_stack[-1] != '(': #( 존재한다면 ( 전까지 스텍 내 연산자들을 다 빼냄. 마지막 ( 도 pop
                    answer += oper_stack.pop() 
                oper_stack.pop()
    
    while oper_stack:
        answer += oper_stack.pop()

    return answer

## input
expr = input()
## output
print(sol(expr))

'''
    for i in range(leng):
        if ord('A') <= ord(expr[i]) <= ord('z'): 
            answer += expr[i] 
            if i == leng-1 : 
                while oper_stack: 
                    answer += oper_stack.pop()
            continue  

        if not oper_stack: oper_stack.append(expr[i]) ; continue
        if expr[i] == '(':
            oper_stack.append(expr[i])
            continue
        if expr[i] == ')':
            while oper_stack:
                p = oper_stack.pop()
                if p == '(': break
                answer += p
            if i == leng-1 : 
                while oper_stack: 
                    answer += oper_stack.pop()
            continue
        
        # if prior[oper_stack[-1]] == 3 : continue

        # 스택의 top이 현재 연산보다 우선순위가 높거나 같을 때
        if prior[oper_stack[-1]] >= prior[expr[i]]:
            if oper_stack[-1] == '(': 
                oper_stack.append(expr[i])
                continue
            while oper_stack: 
                p = oper_stack.pop()
                if p == '(': break
                answer += p
            oper_stack.append(expr[i])
        # 스택의 top이 현재 연산보다 우선순위가 낮을 때
        else : oper_stack.append(expr[i])
    return answer
'''

'''
answer = ''
    oper_stack = []
    prior = {'+':1, '-':1, '*':2, '/':2}
    paren = False

    for i in range(leng):
        # 피연산자는 그냥 기록         
        # 연산자일 때,
            # stack이 비어있으면 push
            # stack의 top과 현재 연산자 중, 
            # top이 더 높거나 같으면 모두 pop, 이후 현재 연산자를 push
            # 현재 연산자가 높으면 push
        # 괄호 '('를 만났을 떄, ')'까지 위와 동일하게 진행
        # ')'를 만났을 때, '('까지 pop
        print(expr[i], oper_stack, answer)
        if ord('A') <= ord(expr[i]) <= ord('z'): answer+=expr[i] ; continue
        # 스텍이 비었거나 top이 ( 일 때를 스텍이 비었다고 판단.
        if not oper_stack or oper_stack[-1] == '(': oper_stack.append(expr[i]) ; continue
        if expr[i] == '(':
            oper_stack.append(expr[i])
            paren = True
            continue
        if expr[i] == ')':
            while oper_stack:
                p = oper_stack.pop()
                if p == '(':break
                answer += p
                if '(' not in oper_stack:
                    paren = False
            continue

        if prior[oper_stack[-1]] >= prior[expr[i]]:
            if paren: # ( 존재 시, ( 전까지만 pop
                while oper_stack and oper_stack[-1] != '(':
                    answer += oper_stack.pop()
                oper_stack.append(expr[i])
            else :
                while oper_stack:
                    answer += oper_stack.pop()
                oper_stack.append(expr[i])

        else : oper_stack.append(expr[i])

    while oper_stack:
        p = oper_stack.pop()
        if p == '(': continue
        answer += p

    return answer
'''