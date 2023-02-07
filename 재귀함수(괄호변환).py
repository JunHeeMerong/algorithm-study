def solution(p):
    U = '' # 리턴용 문자열 생성
    lp=len(p) # 반복문 제어용 길이측정
    count = 0 # 균형잡힌 괄호문자열 슬라이싱용
    i = 0 # 슬라이싱할 인덱스
    while len(U)!=lp: # U가 원래 문자열 p와 길이가 같아질때까지 반복
        if p[i]=='(': # 15열까지가 u,v 분리 count가 다시 0이될때 = 균형잡힌 문자열
            count += 1
        elif p[i]==')':
            count -= 1
        i+=1
        if count==0:
            u = p[:i]
            v = p[i:]
            i = 0
            if u[0]=='(': # u가 올바른 문자열일 경우
                p = v
                U += u
            else: # u가 올바른 문자열이 아닐경우
                if len(v)>0: # v가 존재하면
                    count = 0 # count 초기화 시켜주고
                    v = solution(v) # v를 재귀
                    u = u[1:-1] # 23~27열은 u의 양끝을 제거하고 괄호방향 뒤집기
                    u=u.replace('(','@')
                    u=u.replace(')','(')
                    u=u.replace('@',')')
                    U += '('+v+')'+u # 문자열 조합
                elif len(v) == 0: # v가 존재하지 않으면
                    u = u[1:-1]
                    u=u.replace('(','@')
                    u=u.replace(')','(')
                    u=u.replace('@',')')
                    U += '()'+u # 앞에부분 () 사이에 v가 빈문자열이므로 그대로 조합
    return U