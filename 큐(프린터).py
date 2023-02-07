from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while True:
        if priorities[0] < max(priorities): # 첫번째(제일 왼쪽)에 있는것보다 우선순위가 있는지 확인
            priorities.append(priorities.popleft()) # 있을경우 첫번째 문서를 제일 뒤로 옮긴다.
            if location >= 1: # 우리가 원하는 문서의 위치가 한칸 앞당겨진다.
                location -= 1
            elif location == 0: # 만약 제일 앞이였다면 제일 뒤로 옮긴다.
                location = len(priorities)-1
        elif priorities[0] == max(priorities): # 우선순위의 문서를 찾았을 경우
            priorities.popleft() # 문서를 인쇄하므로 리스트에서 아예 제거
            answer += 1 # 인쇄횟수 +1
            if location >= 1: # 우리가 원하는 문서를 한칸 앞당긴다.
                location -= 1
            elif location == 0: # 만약 0번이라면 지금 뽑은 문서가 인쇄하고 싶은 문서이므로 반복문 종료 후 리턴
                break
    return answer