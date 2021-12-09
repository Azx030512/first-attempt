allGuests={'Alice':{'apples':5,'pretzels':12},
                'Bob':{'ham sandwiches':3,'apples':2},
                'Carol':{'cups':3,'apple pies':1}}
def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought=numBrought+v.get(item,0)
    return numBrought
print('Number of things being brought:')
print(' - Apples                         '+str(totalBrought(allGuests,'apples')))
print(' - Cups                            '+str(totalBrought(allGuests,'cups')))
print(' - Cakes                           '+str(totalBrought(allGuests,'cakes')))
print(' - Ham Sandwiches         '+str(totalBrought(allGuests,'ham sandwiches')))
print(' - Apple Pies                    '+str(totalBrought(allGuests,'apple pies')))


#P98.5.6.1
spam=[]
word=['a','b','c','d','e','f','g','h']
for k in range(1,9):
    for m in word:
        a=str(k)+m
        spam.append(a)
print(spam)

import pprint
def count(keys):
    example={}
    for character in keys:
        example.setdefault(character,0)
        example[character]=example[character]+1
    pprint.pprint(example)
    return example

        

chessman=['bpawn','bknight','bbishop','bbrook','bqueen','bking','wpawn','wknight','wishop','wrook','wqueen','wking']

def isValidChessBoard(board):
    for k in board.keys():
        if k in spam:
            continue
        else:
            return False
            break
    for m in board.values():
        if m in chessman:
            continue
        else:
            return False
            break
    global calculate
    for v in calculate.values():
        if v<8:
            continue
        else:
            return False
            break
    return True
realBoard={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}
calculate=count(list(realBoard.keys()))
asd=isValidChessBoard(realBoard)
print(asd)

        
        
           
        
        
        
        

