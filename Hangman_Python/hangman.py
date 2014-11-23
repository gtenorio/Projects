__author__ = 'Giovanni Tenorio'
#Python implementation of hangman
import sys

def get_secret_word():
	word = input("Please enter a word to be guessed \nthat does not contain ? or white space: ")
	return word

def is_game_over(guess_num):
	if guess_num > 6:
		return True
	else:
		return False

def display_hangman(hangman):
	hangman_s = "".join(hangman)
	print(hangman_s)
	
def display_guesses(guesses):
	print("So far you have guessed: ", end = '')
	for g in sorted(guesses):
		print(g, end = '')
	print()

def get_guess():
	cur_guess = input("Please enter your next guess: ")
	return cur_guess

while True:
	hasSpace = False
	s_word = get_secret_word()
	for s in s_word:
		if s == ' ' or s == '?':
			hasSpace = True
	if hasSpace == False:
		break


board_word = []
for i in s_word:
	board_word.append('?')

hangman = []

guess_num = 0
correct_guess_num = 0

total_guesses = []

while is_game_over(guess_num) == False:
	isCorrect = False
	display_hangman(hangman)
	
	for i in board_word:
		print(i, end = '')
	print()
	
	display_guesses(total_guesses)
	
	while True:
		badGuess = False
		cur_guess = get_guess()
		cur_guess.strip(' ')
		if len(cur_guess) > 1:
			print("You can only guess a single character")
			continue
		for t in total_guesses:
			if cur_guess == t:
				badGuess = True
		if badGuess == True:
			print("You already guessed the character: ", cur_guess)
		else:
			break
		
	count = 0
	for s in s_word:
		if cur_guess == s:
			isCorrect = True
			board_word[count] = s_word[count]
			correct_guess_num += 1	
		count += 1
			
	total_guesses.append(cur_guess)
	if isCorrect == False:
		if guess_num == 0:
			hangman.append(' ')
			hangman.append('|')
			hangman.append(' \n')
		elif guess_num == 1:
			hangman.append(' ')
			hangman.append('0')
			hangman.append(' \n')
		elif guess_num == 2:
			hangman.append(' ')
			hangman.append('|')
			hangman.append(' \n')
		elif guess_num == 3:
			hangman[6] = '/'
		elif guess_num == 4:
			hangman[8] = '\\ \n'
		elif guess_num == 5:
			hangman.append('/')
			hangman.append(' ')
			hangman.append(' \n')
		elif guess_num == 6:
			hangman[11] = '\\ \n'
			display_hangman(hangman)
			print("You failed to guess the secret word: ", s_word)
		guess_num += 1
	
	#end if
	
	if correct_guess_num == len(s_word):
		guess_num = 999
		
		print("YOU GUESSED THE SECRET WORD GG!!!!")
#end big while
