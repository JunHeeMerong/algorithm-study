from collections import deque #popleft를 사용하기 위해 deque import(리스트에서 왼쪽에 있는걸 빼올땐 popleft가 시간소요가 적다.)
n=int(input()) # 일단 몇개의 괄호리스트를 받을것인가에 대한 n값
for i in range(n): # 위에서 받은 n의 수만큼 괄호문제 반복문
    stack=[] # 괄호 리스트에서 하나씩 가져와서 스택리스트에 넣어서 짝이 이뤄질경우 사라지게 만들기 위한 stack 리스트
    l=deque(list(input())) # 괄호 리스트받기
    while l: # 괄호 리스트가 있을경우 계속 반복
        stack.append(l.popleft()) # 괄호 리스트에서 가장왼쪽에 있는 괄호 하나를 stack 리스트로 옮기기
        while len(stack)>=2: # 짝이 이뤄졌을 경우 지워야 하니까 최소 2개의 괄호가 필요하고 2개이상의 괄호가 있을경우 반복문
            if stack[-1]==')' and stack[-2]=='(': # 만약 가장 오른쪽에 있는 2개의 괄호가 '()'모양을 이뤘을 경우 pop2번이용하여 삭제
                stack.pop()
                stack.pop()
            else: # 짝이 아닐경우 무한반복에 빠지므로 braek를 통해 stack while문을 탈출하고 l에서 새로운 괄호를 가져옴
                break
    # 여기까지 왔을경우는 l(괄호리스트)에 모든 괄호를 다 빼왔을때 이므로 이때 스택에 괄호가 남아있는지 확인
    if stack: # 만약 stack에 괄호가 남아있으면 올바른 괄호 문자열이 아니므로 NO
        print('NO')
    else: # 반대경우 즉, stack에 괄호가 없을경우는 모두 짝을 이뤄 삭제되었으므로 올바른 괄호 문자열이므로 YES
        print("YES")