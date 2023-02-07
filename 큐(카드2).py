from collections import deque
n=int(input())
l=deque([i+1 for i in range(n)]) # 카드셋팅(리스트 순서상 왼쪽이 위에, 오른쪽이 아래)
while len(l)>1: # 카드가 한장남을때까지 반복
    l.popleft() # 첫번째 카드를 버린다.
    l.append(l.popleft()) # 두번째 카드는 다시 오른쪽으로 옮긴다.
print(l[0]) # 남은카드