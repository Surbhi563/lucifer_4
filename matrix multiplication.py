print("MULTIPLICATION IS POSSIBLE ONLY WHEN 'no.of columns of first matrix' is equal to 'no. of rows of second matrix'")
y=[] #big matrix for storing row and column matrix
def matrixinput(i):
    print('FOR',i, ' matrix')
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
matrixinput(2)

def matrixmultipication(y):
    l=y[0]
    c=y[3]
    n=len((y[0])[0]) #column of first matrix
    m=len((y[3])[0]) #row of second matrix
    if n==m:
        h=[]
        for i in l:
            m=[]
            for j in c:
                u=0
                k=0
                while k<len(l[0]):
                    u=u+i[k]*j[k]
                    k=k+1
                m.append(u)
            h.append(m)
        print("A X B is")
        for i in h:
            for j in i:
                print(j,' ',end=' ')
            print()
    else:
        print('MULTIPICATION IS NOT POSSIBLE')
        print("MULTIPLICATION IS POSSIBLE ONLY WHEN 'no.of columns of first matrix' is equal to 'no. of rows of second matrix'")
        matrixinput(1)
        matrixinput(2)      
matrixmultipication(y)

      
