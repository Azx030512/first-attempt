message='It is a bright cold day in April , and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character]=count[character]+1
print(count)



import pprint
message='It is bright cold day in April , and the clocks were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)

someDictionaryValue=count
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))

                              
theBoard = {'top-l':'   ','top-m':'   ','top-r':'   ',
                    'mid-l':'   ','mid-m':'   ','mid-r':'   ',
                    'low-l':'   ','low-m':'   ','low-r':'   '}
def printBoard(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['low-l']+'|'+board['low-m']+'|'+board['low-r'])
printBoard(theBoard)
turn='X'
for i in range(9):
    print(Board(theboard))
    print('Turn for '+turn+'.Move on which space?')
    move = input()
    theBoard[move]=turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'
printBoard(theboard)
        
    


