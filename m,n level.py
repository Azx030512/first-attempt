#!python3
MAXN=8
def check(doubleList,m,n):
    found=1
    for j in range(0,m):
        for i in range(j+1,n):
            if doubleList[i][j]!=0:
                found=0
    return found
def operate(doubleList,m,n,k):
    for i in range(k+1,m):

        if doubleList[i][k]!=0:
            cal=doubleList[i][k]/doubleList[k][k]
            for j in range(0,n):
                doubleList[i][j]=doubleList[i][j]-cal*doubleList[k][j]
                print('process')
    return doubleList

import pyinputplus
print('Please enter a determinant')
print('Enter m,n as the length and width:')
m=pyinputplus.inputNum()
n=pyinputplus.inputNum()
doubleList=[]
for i in range(0,m):
    doubleList.append([])
print('Then please enter the number in the determinant in turn .')
for i in range(0,m):
    for j in range(0,n):
        doubleList[i].append(pyinputplus.inputNum())
print(doubleList)
number=0
while check(doubleList,m,n)==0 and number<2:
    for k in range(0,n-1):
        doubleList=operate(doubleList,m,n,k)
    number+=1
for i in range(0,m):
    for j in range(0,n):
        print(doubleList[i][j],end='')
        print('    ',end='')
    print('')
result=1
for k in range(0,m):
    result=result*doubleList[k][k]
print(result)
input()
input()
