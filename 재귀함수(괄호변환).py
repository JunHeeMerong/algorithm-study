def solution(p):
    U = ''
    lp=len(p)
    count = 0
    i = 0
    while len(U)!=lp:
        if p[i]=='(':
            count += 1
        elif p[i]==')':
            count -= 1
        i+=1
        if count==0:
            u = p[:i]
            v = p[i:]
            i = 0
            if u[0]=='(':
                p = v
                U += u
            else:
                if len(v)>0:
                    count = 0
                    v = solution(v)
                    u = u[1:-1]
                    u=u.replace('(','@')
                    u=u.replace(')','(')
                    u=u.replace('@',')')
                    U += '('+v+')'+u
                elif len(v) == 0:
                    u = u[1:-1]
                    u=u.replace('(','@')
                    u=u.replace(')','(')
                    u=u.replace('@',')')
                    U += '()'+u
    return U