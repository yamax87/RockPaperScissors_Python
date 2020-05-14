
"""
Means of player input (rock, paper, scissors)

Means to store player input

Means to respond to player input with a simple, variable condition

Means to vary the condition, eg with a random() function

Means to check whether player's input beats or matches computer input

Means to keep score

"""

"""
#new architecture: GENERAL APPROACH
#-call each function

def func1():
    # do stuff
    callfunc3 = input('Call 3rd function? Y/N').upper()
    if callfunc3 = 'Y':
		a = 2
		print(f'the local value of a is: {a}')

print('the global value of a is: {a}')
    

def func2():
	print('func2 was called.')
    # do more stuff

def func3():
	print('func3 was called.')
    # something completely different
    

a = 1

while a == 1: # this will loop indefinately, unless one of the functions chages "a"
    func1()
    func2()
    func3()
    

#create global variables to change a

"""

from random import randint 
import sys

rockPaperScissorsList = ['R','P','S']

scoreBoard = {
	'computer' : 0,
	'player' : 0,
}

playGame = True

def playerInputFunc(rockPaperScissorsList):
	while True:
		global playerInput
		#playerInput = str(input('Enter your choice of rock, paper or scissors. (R, P or S):\n')).upper()
		playerInput = 'P'
		if playerInput in rockPaperScissorsList:
			break
		print('Nope, that is neither a rock, nor a paper, nor a scissors, bud.')

def computerInputFunc(rockPaperScissorsList):
	selection = randint(0,2)
	global computerInput
	computerInput = rockPaperScissorsList[selection]
	
def checkResult(computerInput, playerInput):
	global computer_Wins
	global player_Wins
	computer_Wins = False
	player_Wins = False
	#print(computerInput_param, playerInput_param)
	if computerInput == playerInput:
		print('Draw.')
	elif computerInput == 'R':
		if playerInput == 'P':
			player_Wins = True
		if playerInput == 'S':
			computer_Wins = True
	elif computerInput == 'P':
		if playerInput == 'S':
			player_Wins = True
		if playerInput == 'R':
			computer_Wins = True
	elif computerInput == 'S':
		if playerInput == 'R':
			player_Wins = True
		if playerInput == 'P':
			computer_Wins = True
			
	#computer_Wins=True
	#playAgainSelector(computer_Wins, player_Wins, scoreBoard)	
	#print(computer_Wins)
	
			
def playAgainSelector(computer_Wins, player_Wins, scoreBoard):
	#computer_round_result_param = False
	if computer_Wins == True:
		print('You lose, sweetykittens.')
		scoreBoard['computer'] += 1
	if player_Wins == True:
		print('You win! Grab some flat diet coke or something!')
		scoreBoard['player'] += 1
	if (player_Wins == False) and (computer_Wins == False):
		print('A draw. How boring. Not even the one you keep your socks in. Ah, well.') 
	print('The score is:')
	print(f"\tcomputer - {scoreBoard['computer']}")
	print(f"\tplayer - {scoreBoard['player']}")
	print('\n')
	
	while True:
		#playAgain = str(input('Play again? Y/N \n'))
		playAgain = 'Y'
		global playGame
		playGame = True
		if playAgain.upper() == 'Y':
			break
		elif playAgain.upper() == 'N':
			playGame = False
			break
		else: 
			print('That didn\'t look like a yes or a no, so we\'re back to asking the same question, mm\'kay?')
			

while playGame == True:
	playerInputFunc(rockPaperScissorsList)
	computerInputFunc(rockPaperScissorsList)
	checkResult(computerInput,playerInput)
	playAgainSelector(computer_Wins, player_Wins, scoreBoard)
	
if playGame == False:
	print('Ok, it was boring for me too, you know...')
	sys.exit()
	

	
	
