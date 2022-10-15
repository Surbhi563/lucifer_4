def matrix():
    y=[] #big matrix for storing row and column matrix
    def matrixinput(i):
        print('ENTER UR MATRIX')
        m=int(input('no. of rows'))
        n=int(input('no. of columns'))
        l=[]    #row matrix
        for i in range(1,m+1):
            print(i,'row input')
            row=[]
            for j in range(n):
                x=float(input('enter entries'))
                row.append(x)
            l.append(row)
        print('matrix u entered')
        for i in l:
            for j in i:
                print(j,' ',end=' ')
            print()
        c=[] #column matrix
        k=0
        while k<len(l[0]):
            h=[]
            for i in l:
                h.append(i[k])
            c.append(h)
            k=k+1
        y.append(l)
        y.append(c)
    matrixinput(1)
    def determinantnXn(n,l):
        if len(l)==len(l[0]):
            k=0
            if n==2:
                a=l[0][0]
                b=l[0][1]
                c=l[1][0]
                d=l[1][1]
                x=a*d-b*c
                return x
            else:
                for i in l[0]:
                    d=[]
                    x=l[0].index(i)
                    for j in l[1:]:
                        t=j[x]
                        j.remove(j[x])
                        v=j[0:]
                        d.append(v)
                        j.insert(x,t)
                    k=k+(i*(-1)**(x)*(determinantnXn(n-1,d)))
            return k
        else:
            print("U DIDN'T ENETER NxN ORDER MATRIX")
            matrix()
        
    g=determinantnXn(len(y[0]),y[0])
    print(g)
matrix()

































    
