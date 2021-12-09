import random,sys
print('Rock,Paper,Scissors')
wins = 0
losses = 0
ties = 0
while True :
    print('%s Wins,  %s  Losses,  %s  Ties'  %  (wins,  losses,  ties))
    while True:
        print('Enter your move: rock  paper  scissors  or  quit')
        playerMove = input()
        if playerMove == 'quit':
            sys.exit()
        elif playerMove =='rock' or playerMove == 'paper' or playerMove == 'scissors':
            break
        print('Please type one of rock, paper or scissors')
    if playerMove =='rock':
        print('Rock versus ...')
    elif playerMove =='paper':
        print('Paper versus ...')
    elif playerMove =='scissors':
        print('Scissors versus ..')
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'rock'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'paper'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 'scissors'
        print('Scissors')
    if playerMove == computerMove:
        print('It is a tie!')
        ties=ties + 1
    elif playerMove == 'rock' and computerMove == 'scissors':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'rock' and computerMove == 'paper':
        print('You lose!')
        losses=losses +1
    elif playerMove == 'paper' and computerMove == 'rock':
        print('You win!')
        wins=wins + 1
    elif playerMove == 'paper' and computerMove == 'scissors':
        print('You lose!')
        losses=losses + 1
    elif playerMove == 'scissors' and computerMove == 'rock':
        print('You lose!')
        losses =losses + 1
    elif playerMove == 'scissors' and computerMove == 'paper':
        print('You win!')
        losses=losses + 1
        
