def f(x):
    y=''
    for i in range(len(x)-1):
        y=y+x[i]+', '
    y+='and '
    y+=x[len(x)-1]
    print(y)
spam=['apple','bananas','tofu','cats']
f(spam)


import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    #code that creates a list of 100 'heads' or 'tails' values.
    exampleList = []
    for i in range(100):
        exampleList.append(random.randint(0,1))
    #code that checks if there is a streak of 6 heads or tails in a row
    for x in range(94):
        if exampleList[x]==0 and exampleList[x+1]==0 and exampleList[x+2]==0 and exampleList[x+3]==0 and exampleList[x+4]==0 and exampleList[x+5]==0:
            numberOfStreaks+=1
            break
print('Chance of streak: %s%%' %(numberOfStreaks/100))


grid=[['. ','. ','. ','. ','. ','. '],
          ['. ','0','0','. ','. ','. '],
          ['0','0','0','0','. ','. '],
          ['0','0','0','0','0','. '],
          ['. ','0','0','0','0','0'],
          ['0','0','0','0','0','. '],
          ['0','0','0','0','. ','. '],
          ['. ','0','0','. ','. ','. '],
          ['. ','. ','. ','. ','. ','. ']]
import copy
picture=copy.deepcopy(grid)
for y in range(6):
    for x in range(9):
        print(picture[x][y],end=' ')
    print('')
