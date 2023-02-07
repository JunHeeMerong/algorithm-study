from collections import deque
n=int(input())
for i in range(n):
    stack=[]
    l=deque(list(input()))
    while l:
        stack.append(l.popleft())
        while len(stack)>=2:
            if stack[-1]==')' and stack[-2]=='(':
                stack.pop()
                stack.pop()
            else:
                break
    if stack:
        print('NO')
    else:
        print("YES")