import random

UserWins = 0
ComputerWins = 0

options = ['rock', 'paper', 'scissors']

while True:
    UserInput = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if UserInput == 'q':
        quit()
    if UserInput not in ['rock', 'paper', 'scissors']:
        continue
    RandomNumber = random.randrange(3)
    #rock: 0, paper: 1, scissors: 2 
    ComputerPick = options[RandomNumber]
    print('Computer picked', ComputerPick + '.')

    if UserInput == 'rock' and ComputerPick == 'scissors':
        print('You won!')
        UserWins += 1
        continue

    elif UserInput == 'paper' and ComputerPick == 'rock':
        print('You Won!')
        UserWins += 1

    elif UserInput == 'scissors' and ComputerPick == 'paper':
        print('You won!')
        UserWins += 1

    else:
        print('You lost!')
        ComputerWins += 1

print('You won', UserWins, 'times.')
print('The computer won', ComputerWins, 'times.')
print('Goodbye!')
    
