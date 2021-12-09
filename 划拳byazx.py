print('划拳程序  by  azx')
import random,sys
while True:
    print('Please type a number from 0 to 5 as your response.')
    playerNumber1=input()
    print('Please type a number from 0 to 10 as your guess total number.')
    playerNumber2=input()
    if int(playerNumber1)>5 or int(playerNumber1)<0:
        print('You got it wrong!')
        continue
    elif int(playerNumber1)>=0 and int(playerNumber1)<=5:
        computerNumber1=random.randint(0,5)
        computerNumber2=random.randint(0,10)
        if computerNumber2<=computerNumber1:
            print('computer has got it wrong, please try again.')
            continue
        #print(computerNumber1)
        print('computer gives out a '+str(computerNumber1))
       # print(computerNumber2)
        print('computer guess the total number is '+str(computerNumber2))
        totalNumber=int(playerNumber1) + computerNumber1
        print('real total number is '+str(totalNumber))
        if int(playerNumber2)==totalNumber and int(computerNumber2)==totalNumber:
            print('You both win!')
        elif int(playerNumber2)!=totalNumber and int(computerNumber2)==totalNumber:
            print('You lose!')
        elif int(playerNumber2)==totalNumber and int(computerNumber2)!=totalNumber:
            print('You win!')
        else:
            print('You and the computer both did not get it right')
    input()
            
            
        
        
              
