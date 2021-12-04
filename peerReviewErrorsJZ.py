# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jose Zamorano
# Creation Date: 1 December 2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

##import Identity function is not being used Zamorano (9)
import random 
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')

	##Why is there a blank print here? - Zamorano (11)

def chooseCave():
	##Indented incorrectly. - Zamorano (4)
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
	## Not returning 'cave' user input error. - Zamorano (3)
	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	## Not actually sleeping for 2 seconds here like you wrote in the comment, fixed it - Zamorano (12)
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	
	## Another blank print here?? - Zamorano (2)
	print()

	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		##Missing parethesis (5)
		print ('Gobbles you down in one bite!')

## This should all be in a main() and then main() should be called. (8)
# Missing double equals sign - Zamorano(1)
def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':

		displayIntro()
		##Choose cave syntax error it needed a captial C in 'Cave' (6)
		caveNumber = chooseCave()
		checkCave(caveNumber)

		print('Do you want to play again? (yes or no)')
		playAgain = input()

		if playAgain == "no":

			##User spelled 'playing' incorrectly. (7)
	 		print("Thanks for planing")
	
main()
	

