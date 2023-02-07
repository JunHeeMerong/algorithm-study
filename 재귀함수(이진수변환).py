answer = '' # 정답용 빈 string

def bin_num(n): # 재귀함수
    global answer
    a=n%2 # 2로 나눴을때 나머지(0 or 1)를 오른쪽부터 하나씩
    answer=str(a)+answer
    n=(n-a)//2 # 2번째 자리는 2제곱, 3번째 자리는 3제곱 대신 나머지(a)를 빼고 2로 나눠서 반복
    if n==0: # n = 0 일경우 함수종료
        return print(answer)
    else: # n > 0 일경우 다시 함수에 넣어서 반복
        return bin_num(n)
n=int(input())
bin_num(n)

#-------------------------------------------------------
# 재귀함수 말고 그냥 2진법함수(bin) 활용
# print(bin(int(input()))[2:])
# 설명↓
# input으로 10진법 숫자를 받아서 bin을 사용할 경우 0b~~~~~~ 식으로 2진수가 나오므로
# 0b를 제외한 나머지를 출력하기위해 [2:] 사용