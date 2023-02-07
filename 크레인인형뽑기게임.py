def solution(board, moves):
    answer = 0 # 점수(짝을 맞춘 인형의 개수)
    box = [] # board에서 하나씩 꺼내 담을 box리스트
    for i in moves: # move리스트에서 앞에 숫자를 하나씩 추출
        for j in range(len(board)): # j는 보드의 위에칸부터
            if board[j][i-1] == 0: # 리스트의 첫 인덱스는 0부터 시작이므로 i-1 / 만약 0이라면 없는것이므로 j를 키워서 더 아래칸을 확인
                continue
            elif board[j][i-1] != 0: # 0이 아닐경우 인형이 존재 하는것이므로 borad에서 꺼내서 box에 추가하고 0으로 바꾼다.
                box.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(box) > 1: # box에 2개 이상의 인형이 있을경우
            if box[-1] == box[-2]: # 맨위(리스트상에서는 제일 오른쪽) 2개의 인형이 같을경우 2개를 제거하고 점수2점 추가
                box.pop()
                box.pop()
                answer += 2
    return answer