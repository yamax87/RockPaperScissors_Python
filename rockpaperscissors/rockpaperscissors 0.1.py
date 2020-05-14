
"""
Means of player input (rock, paper, scissors)

Means to store player input

Means to respond to player input with a simple, variable condition

Means to vary the condition, eg with a random() function

Means to check whether player's input beats or matches computer input

Means to keep score

"""

from random import randint 
from time import sleep
import sys

rockPaperScissorsList = ['R','P','S']

scoreBoard = {
	'computer' : 0,
	'player' : 0,
}

def playerInputFunc(rockPaperScissorsList_param):
	while True:
		#playerInput = str(input('Enter your choice of rock, paper or scissors. (R, P or S):\n')).upper()
		playerInput = "R"
		if playerInput in rockPaperScissorsList:
			return computerInputFunc(rockPaperScissorsList, playerInput)
		print('Nope, that is neither a rock, nor a paper, nor a scissors, bud.')

def computerInputFunc(rockPaperScissorsList_param, playerInput_param):
	selection = randint(0,2)
	computerResponse = rockPaperScissorsList[selection]
	return checkResult(computerResponse, playerInput_param)
	
def checkResult(computerInput_param, playerInput_param):
	computer_wins = False
	player_wins = False
	#print(computerInput_param, playerInput_param)
	if computerInput_param == playerInput_param:
		print('Draw.')
	elif computerInput_param == 'R':
		if playerInput_param == 'P':
			player_wins = True
		if playerInput_param == 'S':
			computer_wins = True
	elif computerInput_param == 'P':
		if playerInput_param == 'S':
			player_wins = True
		if playerInput_param == 'R':
			computer_wins = True
	elif computerInput_param == 'S':
		if playerInput_param == 'R':
			player_wins = True
		if playerInput_param == 'P':
			computer_wins = True
			
	#computer_wins=True
	playAgainSelector(computer_wins, player_wins, scoreBoard)	
	#print(computer_wins)
	
			
def playAgainSelector(computer_round_result_param, player_round_result_param, scoreBoard_param):
	#computer_round_result_param = False
	if computer_round_result_param == True:
		print('You lose, sweetykittens.')
		scoreBoard_param['computer'] += 1
	if player_round_result_param == True:
		print('You win! Grab some flat diet coke or something!')
		scoreBoard_param['player'] += 1
	if player_round_result_param == False and computer_round_result_param == False:
		print('A draw. How boring. Not even the one you keep your socks in. Ah, well.') 
	print('The score is:')
	print(f"\tcomputer - {scoreBoard_param['computer']}")
	print(f"\tplayer - {scoreBoard_param['player']}")
	print('\n')
	
	while True:
		#playAgain = str(input('Play again? Y/N \n'))
		playAgain = "Y"
		if playAgain.upper() == 'Y':
			playerInputFunc(rockPaperScissorsList)
		elif playAgain.upper() == 'N':
			print('Ok, it was boring for me too, you know...')
			sys.exit()
		else: 
			print('That didn\'t look like a yes or a no, so we\'re back to asking the same question, mm\'kay?')
			
	
playerInputFunc(rockPaperScissorsList)
	
	
	
