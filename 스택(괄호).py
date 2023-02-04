n=int(input())
for i in range(n):
    V_list = list(input())
    sum = 0
    cnt=1
    for j in V_list:
        if j == '(':
            sum+=1
        elif j == ')':
            sum-=1
        
        if sum<0:
            print('NO')
            cnt=0
            break
    if cnt==0:
        continue
    if sum != 0:
        print('NO')
    else:
        print('YES')