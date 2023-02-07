f=1 # 팩토리얼 계산 초기값
i=1 # 1부터 증가용 계산 초기값
def fac(n): # 팩토리얼 재귀함수
    global f,i
    if n==0: # 만약 n = 0 이면 0!=1 이므로 그냥 1로 리턴
        return print(1)
    if i==n: # i 가 원하는 n값까지 증가했을 경우 f(팩토리얼 계산값)을 리턴 후 종료
        return print(f)
    else: # i는 1씩 증가, f는 팩토리얼 계산 후 다시 함수로 재귀
        i+=1
        f*=i
        return fac(n)
n=int(input())
fac(n)

#-------------------------------------
# 단순 반복문으로 계산
# n=int(input())
# f=1
# if n != 0: # n=0일경우 0!=1이므로 반복문 안하고 바로 f값 출력
#     for i in range(n): # range는 0부터 이므로 아래서 (i+1)로 팩토리얼계산
#         f=f*(i+1)
# print(f)