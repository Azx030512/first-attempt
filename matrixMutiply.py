#!python3
#matrixMutiply.exe -- This function can mutiply two matrix
def device(i,j,a,b):
    result=0
    for m in range(0,len(b)):
        result+=a[i][m]*b[m][j]
    return result
a=[]
b=[]
c=[]
print('Please input the length and width of the two matrx seperately.')
print('Let me give you an example.')
print(r'''                            width
                         4   8   2    3      4
                         3   4   5    6      27
        length       5   5   8    7      1
                        4     0   6    7      -2
                        ''')
print('Input the first matrix\'s length and width.')
length1=int(input())
width1=int(input())
print('Input the second matrix\'s length and width.')
length2=int(input())
width2=int(input())
print('Then enter the matrix element in turn.')
for i in range(0,length1):
    a.append([])
    for j in range(0,width1):
        a[i].append(int(input()))
print('Then enter the next matrix.')
for i in range(0,length2):
    b.append([])
    for j in range(0,width2):
        b[i].append(int(input()))
length3=length1
width3=width2
for i in range(0,length1):
    c.append([])
    for j in range(0,width1):
        c[i].append(device(i,j,a,b))
for i in range(0,length1):
    for j in range(0,width1):
        print(c[i][j],end='')
        print(' ',end='')
    print('')
